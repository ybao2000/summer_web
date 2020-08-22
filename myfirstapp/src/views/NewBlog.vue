<template>
  <div>
    <h3>New Blog</h3>
      <div class="form-group ml-5 mr-5">
        <label for="title" class="mt-3">Title</label>
        <input type="text" class="form-control" id="title" v-model="blog.title">

        <label for="image" class="mt-3">Select Image</label>
        <select class="form-control" id="image" v-model="blog.image">
          <option value="blog1.jpg">cate 1</option>
          <option value="blog2.jpg">cate 2</option>
          <option value="blog3.jpg">cate 3</option>
          <option value="blog4.jpg">cate 4</option>
          <option value="blog5.jpg">cate 5</option>
        </select>

        <label for="content" class="mt-3">Content</label>
        <textarea class="form-control" id="content" rows="10" v-model="blog.content"></textarea>
      </div>
      <button type="submit" class="btn btn-primary" @click.prevent="submit()">Submit</button>
  </div>
</template>

<script>
import axios from 'axios'
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
      var formData = new FormData()
      formData.set('title', this.blog.title)
      formData.set('content', this.blog.content)
      formData.set('image', this.blog.image)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/addblog',
        data: formData,
        headers: { 'Content-Type': 'multipart/form-data', 'Access-Control-Allow-Methods': 'GET,POST,OPTIONS' }
      }).then(res => {
        console.log(res)
        this.addBlog(this.blog) // this one is to tell the store to do the change
        this.$router.push({ name: 'BlogList' }) // this one is to jump to another page
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>
