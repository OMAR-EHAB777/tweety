<template>
  <div class="example">
    <h1>first single file componnet</h1>
      <h3>{{ message }}</h3>
  </div>
</template>
<script>
    export default{
        name:"example",
        data() {
            return{
                message:"helloword!"
            }
        }
    }
</script>
<style scoped>
    h1{
        color:red;
    }
</style>