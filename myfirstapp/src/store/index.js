import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    blogs: [
    ]
  },
  modules: {
  },
  getters: {
    allBlogs (state) {
      return state.blogs
    }
  },
  mutations: {
    // this one is doing the real operation, i.e., add the blog into the store
    addBlog (state, blog) {
      state.blogs.push(blog)
    },
    initBlogs (state, mblogs) {
      state.blogs = mblogs
    }
  },
  actions: {
    addBlog (context, blog) {
      // this one is to inform the mutation about the change
      context.commit('addBlog', blog)
    },
    initBlogs (context, mblogs) {
      context.commit('initBlogs', mblogs)
    }
  }
})
