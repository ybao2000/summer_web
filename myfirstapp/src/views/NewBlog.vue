<template>
  <div>
    <h3>New Blog</h3>

    <form>
      <div class="form-group ml-5 mr-5">
        <label for="title" class="mt-3">Title</label>
        <input type="text" class="form-control" id="title">

        <label for="image" class="mt-3">Select Image</label>
        <select class="form-control" id="image">
          <option value="blog1.jpg">cate 1</option>
          <option value="blog2.jpg">cate 2</option>
          <option value="blog3.jpg">cate 3</option>
          <option value="blog4.jpg">cate 4</option>
          <option value="blog5.jpg">cate 5</option>
        </select>

        <label for="content" class="mt-3">Content</label>
        <textarea class="form-control" id="content" rows="10"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>
