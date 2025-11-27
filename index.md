---
layout: default
title: Test
---

# Jekyll GitHub LFS Test

This is a test page to verify Jekyll + GitHub Pages + GitHub LFS works.

1. Referencing a GitHub LFS resource directly results in 404 on GitHub Pages (it works locally)

   ![Test Image](/images/test.png)

2. Referencing a full URL of a GitHub LFS resource works

   ![Test Image with absolute path](https://media.githubusercontent.com/media/marcindulak/jekyll-github-lfs/refs/heads/main/images/test.png)

3. Referencing a GitHub LFS resource through a Jekyll filter works

   ![Test Image with a Jekyll filter]({{ '/images/test.png' | lfs_url }})
