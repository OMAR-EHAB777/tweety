<template>
<div class="single-tweet mt-2">
    <div class="container">
       <div class="card gedf-card">
        <div class="card-header">
        <div class="d-flex justify-content-between align-items-center">
            <div class="d-flex justify-content-between align-items-center">
            <div class="mr-2">
                <img class="rounded-circle" width="45" src="https://picsum.photos/50/50" alt="">
            </div>
            <div class="ml-2">
                <div class="h7 text-muted">{{ tweets.author }}</div>
            </div>
        </div>
                    <div>
                    </div>
                </div>

            </div>
            <div class="card-body">
                <div class="text-muted h7 mb-2"> <i class="fa fa-clock-o"></i>{{ tweets.created_at }}</div>
                <p class="card-text">
                    {{ tweets.content }}
                </p>
            </div>
            <div class="card-footer">
                <a href="#" class="card-link"><i class="fa fa-gittip"></i> Like</a>
                <a href="#" class="card-link"><i class="fa fa-comment"></i> {{ tweets.comments_count }}</a>
                <a href="#" class="card-link"><i class="fa fa-mail-forward"></i> Share</a>
            </div>
        </div>
        <hr>
         <div v-if="userHascommenteded">
        <p class="answer-added">You've written an answer!</p>
      </div>
      <div v-else-if="showForm">
        <form class="card" @submit.prevent="onSubmit">
          <div class="card-header px-3">
            Answer the Question
          </div>
          <div class="card-block">
            <textarea
              v-model="newcommentbody"
              class="form-control"
              placeholder="Share Your Knowledge!"
              rows="5"
            ></textarea>
          </div>
          <div class="card-footer px-3">
            <button type="submit" class="btn btn-sm btn-success">Submit Your Answer</button>
          </div>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
      </div>
      <div v-else>
        <button
          class="btn btn-sm btn-success"
          @click="showForm = true"
          >Answer the Question
        </button>
      </div>
      <hr>
    </div>
        <div class="container">
            <commentComponent
              v-for="(comments, index) in comments"
              :comments="comments"
              :requestUser="requestUser"
              :key="index"
              @delete-comment="deletecomment"
            />
        </div>
    <div class="my-4">
        <p v-show="loadingcomments">...loading...</p>
        <button
          v-show="next"
          @click="gettweetscomment"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>

</template>
<script>
import { apiService } from "@/common/api.service.js";
import commentComponent from "@/components/comment.vue";
export default {
 name: "Tweetty",
 props: {
    slug: {
        type: String,
        required: true

    }
  },
  components: {
    commentComponent

  },
 data() {
    return {
      tweets: {},
      comments:[],
      newcommentbody: null,
      error: null,
      userHascommenteded: false,
      showForm: false,
      next: null,
      loadingcomments: false,
      requestUser: null
    }
 },

 methods:{
         setPageTitle(title) {
      // set a given title string as the webpage title
              document.title = title;
            },
          setRequestUser() {
      // the username has been set to localStorage by the App.vue component
          this.requestUser = window.localStorage.getItem("username");
    },
         gettweetsData() {
      // get the details of a question instance from the REST API and call setPageTitle
          let endpoint = `/api/tweets/${ this.slug }/`;
          apiService(endpoint)
            .then(data => {
                this.tweets = data;
                this.userHascommenteded = data.user_has_commented;
                this.setPageTitle(data.content)
        })
         },
        gettweetscomment(){
             let endpoint = `/api/tweets/${this.slug}/comments/`;
               if (this.next) {
                endpoint = this.next;
              }
              this.loadingcomments = true;
              apiService(endpoint)
               .then(data => {
                  this.comments.push(...data.results);
                    this.loadingcomments = false;
                      if (data.next) {
                        this.next = data.next;
                      } else {
                        this.next = null;
                      }
        })

        },
    onSubmit() {
      // Tell the REST API to create a new answer for this question based on the user input, then update some data properties
      if (this.newcommentbody) {
        let endpoint = `/api/tweets/${this.slug}/comment/`;
        apiService(endpoint, "POST", { body: this.newcommentbody })
          .then(data => {
            this.comments.unshift(data)
          })
        this.newcommentbody = null;
        this.showForm = false;
        this.userHascommented = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty answer!";
      }
    },
      async deletecomment(comments) {
      // delete a given comment from the comments array and make a delete request to the REST API
      let endpoint = `/api/comments/${comments.id}/`;
      try {
        await apiService(endpoint, "DELETE")
        this.$delete(this.comments, this.comments.indexOf(comments))
        this.userHascommented = false;
      }
      catch (err) {
        console.log(err)
      }
    }
 },
  created() {
    this.gettweetsData()
    this.gettweetscomment()
    this.setRequestUser()
  }
};
</script>
<style>

</style>