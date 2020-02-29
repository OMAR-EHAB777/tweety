<template>
<div class="container">
            <form @submit.prevent="onSubmit">
                <textarea
                          v-model="tweety_body"
                          rows="3"
                          class="form-control"
                          placeholder="What are you thinking?">
                </textarea>
            <br>
            <button
                type="submit"
                class="btn btn-success"
                >Publish
              </button>

         </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
              </div>





</template>
<script>
import { apiService } from "@/common/api.service.js";
export default{
    name :"TweettyEditor",
<<<<<<< HEAD
     props: {
=======
    props: {
>>>>>>> 26f21e2502eb7d7a4b6bbf2bc12d07ddecc9336b
     slug: {
        type: String,
        required: false
    }
  },
    data() {
            return {
               tweety_body: null,
               error: null

           }
    },
    methods:{
         onSubmit() {
              // Tell the REST API to create or update a Question Instance
              if (!this.tweety_body) {
                this.error = "You can't send an empty tweety!";
              } else if (this.tweety_body.length > 240) {
                this.error = "Ensure this field has no more than 240 characters!";
              } else {
                let endpoint = "/api/tweets/";
                let method = "POST";
                apiService(endpoint, method, { content: this.tweety_body })
                  .then(tweets_data => {
                    this.$router.push({
                    name: 'tweety',
                    params: { slug: tweets_data.slug }
                })
            })
         }
      }
    },
        created() {
            document.title = "Editor - tweety";
         }
    };
</script>
<style>

</style>