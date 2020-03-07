<template>
<div class="single-comment">
    <p class="text-muted">
      <strong>{{ comments.author }}</strong> &#8901; {{ comments.created_at }}
    </p>
    <p>{{ comments.body }}</p>
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
   }
 }
}

</script>