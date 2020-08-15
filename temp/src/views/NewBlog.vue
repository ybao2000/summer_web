<template>
  <div>
    <h3>New Blog</h3>
    <form class="mt-3">
      <div class="form-group ml-5 mr-5">
        <label for="title">Title</label>
        <input type="text" class="form-control mb-3" id="title" aria-describedby="emailHelp" placeholder="Enter title" v-model="blog.title">
        <label for="image">Image</label>
        <select class="form-control mb-3" id="image" v-model="blog.image">
          <option value="blog1.jpg">blog1</option>
          <option value="blog2.jpg">blog2</option>
          <option value="blog3.jpg">blog3</option>
          <option value="blog4.jpg">blog4</option>
        </select>
        <label for="content">content</label>
        <textarea class="form-control" id="content" rows="10" v-model="blog.content"></textarea>
      </div>
      <button type="submit" class="btn btn-primary" @click.prevent="submit()">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  data () {
    return {
      blog: {
        title: '',
        content: '',
        image: 'blog1.jpg'
      }
    }
  },
  methods: {
    ...mapActions(['addBlog']),
    submit () {
      // console.log(this.blog)
      this.addBlog(this.blog)
      this.$router.push({ name: 'BlogList' })
    }
  }
}
</script>
