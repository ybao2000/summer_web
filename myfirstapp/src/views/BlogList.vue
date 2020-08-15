<template>
  <div>
    Blogs
    <div class="card mb-3 ml-5" style="max-width: 80%;" v-for="blog in blogs" :key="blog.id">
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
export default {
  data () {
    return {
      blogs: [
        {
          id: 1,
          title: 'Title 1',
          content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
          author: 'Frank Bao',
          date: 'Aug 14th, 2020',
          image: 'blog1.jpg'
        },
        {
          id: 2,
          title: 'Title 2',
          content: 'This is blog content for title 2',
          author: 'Frank Bao',
          date: 'Aug 15th, 2020',
          image: 'blog2.jpg'
        },
        {
          id: 3,
          title: 'Title 3',
          content: 'This is blog content for title 3',
          author: 'Frank Bao',
          date: 'Aug 16th, 2020',
          image: 'blog3.jpg'
        },
        {
          id: 4,
          title: 'Title 4',
          content: 'This is blog content for title 4',
          author: 'Frank Bao',
          date: 'Aug 17th, 2020',
          image: 'blog4.jpg'
        }
      ]
    }
  }
}
</script>
