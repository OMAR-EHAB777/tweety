<template>
<div class="single-comment">
    <p class="text-muted">
      <strong>{{ comments.author }}</strong> &#8901; {{ comments.created_at }}
    </p>
    <p>{{ comments.body }}</p>
    <div v-if="iscommentsAuthor">
      <button>edit</button>
    
     </div>
     <button class="btn btn-sm btn-outline-danger"
            @click="triggerDeletecomment">delete</button>
<hr>
</div>
</template>
<script>
export default {
  name: "commentComponent",
  props: {
    comments: {
     type: Object,
     required: true
   },
   requestUser: {
      type: String,
      required: true
    }
 },
 computed: {
    iscommentsAuthor() {
      // return true if the logged in user is also the author of the comment instance
      return this.comments.author === this.requestUser;
    }
  },
   methods: {
     triggerDeletecomment() {
      // emit an event to delete an comment instance
      this.$emit("delete-comment", this.comments)
    }
   }
}

</script>