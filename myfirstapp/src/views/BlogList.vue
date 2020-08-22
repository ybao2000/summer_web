<template>
  <div>
    <div>
      <span class="h3 mr-5">Blogs</span>
      <router-link to="/newblog" class="btn btn-primary btn-sm mt-1 mb-1" >
        <i class="fas fa-plus-circle"></i>New Blog
      </router-link>
    </div>
    <div class="card mb-3 ml-5 mt-2" style="max-width: 80%;" v-for="blog in allBlogs" :key="blog.id">
      <div class="row no-gutters">
        <div class="col-md-4">
          <img :src="'/images/'+blog.image" class="card-img" alt="Image">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">{{ blog.title }}</h5>
            <p class="card-text">{{ blog.content }}</p>
            <p class="card-text"><small class="text-muted">{{ blog.author }}</small></p>
            <p class="card-text"><small class="text-muted">{{ blog.date }}</small></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'

export default {
  data () {
    return {
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/blogs')
      .then(response => {
        console.log(response.data)
        this.initBlogs(response.data)
      })
  },
  methods: {
    ...mapActions(['initBlogs'])
  },
  computed: mapGetters(['allBlogs'])
}
</script>
