<template>
<div class="home">
<!-- Post /////-->
<div class="container">
 <div v-for="tweets in tweets"
    :key="tweets.pk">
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
                        <div class="dropdown">
                            <button class="btn btn-link dropdown-toggle" type="button" id="gedf-drop1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                <i class="fa fa-ellipsis-h"></i>
                            </button>
                            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="gedf-drop1">
                                <div class="h6 dropdown-header">Configuration</div>
                                <a class="dropdown-item" href="#">Save</a>
                                <a class="dropdown-item" href="#">Hide</a>
                                <a class="dropdown-item" href="#">Report</a>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="card-body">
                <div class="text-muted h7 mb-2"> <i class="fa fa-clock-o"></i>{{ tweets.created_at }}</div>
                <a class="card-link" href="#">
                    <h5 class="card-title">Lorem ipsum dolor sit amet, consectetur adip.</h5>
                </a>

                <p class="card-text">
                    <router-link
                        :to="{ name: 'tweety', params: { slug: tweets.slug } }"
                       class="tweets-link"
                      >{{ tweets.content }}
                   </router-link>
                </p>
            </div>
            <div class="card-footer">
                <a href="#" class="card-link"><i class="fa fa-gittip"></i> Like</a>
                <a href="#" class="card-link"><i class="fa fa-comment"></i> {{ tweets.comments_count }}</a>
                <a href="#" class="card-link"><i class="fa fa-mail-forward"></i> Share</a>
            </div>
        </div>
 </div>
<div class="my-4">
        <p v-show="loadingtweets">...loading...</p>
        <button
          v-show="next"
          @click="gettweets"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
</div>
</div>
</div>      <!-- Post /////-->
</template>
<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "home",
   data() {
       return {
            tweets: [],
            next: null,
            loadingtweets: false
       }
},
methods: {
    gettweets() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/tweets/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingtweets = true;
      apiService(endpoint)
        .then(data => {
          this.tweets.push(...data.results)
          this.loadingtweets = false;
           if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    }
    },
  created() {
    this.gettweets()
    document.title = "Tweety";
  }
};
</script>
<style scoped>
</style>