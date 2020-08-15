<template>
  <div>
    <div class="mb-3">
      <span class="h3 mr-5">Blogs</span>
      <router-link to="/newblog" class="btn btn-primary btn-sm mt-1 mb-1">
        <i class="fa fa-plus-circle"></i> New Blog
      </router-link>
    </div>
    <div class="card ml-5 mb-2" style="max-width: 80%;" v-for="blog in allBlogs" :key="blog.id">
      <div class="row">
        <div class="col-md-12">
          <h5 class="text-center text-primary mt-2">{{ blog.title }}</h5>
        </div>
      </div>
      <div class="row no-gutters">
        <div class="col-md-4">
          <img
              style="width: 200px"
              :src="'images/'+blog.image"
            alt="Avatar of Jonathan Reinink"
          />
        </div>
        <div class="col-md-8">
          <div class="card-body">
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
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
    }
  },
  computed: mapGetters(['allBlogs'])
}
</script>
