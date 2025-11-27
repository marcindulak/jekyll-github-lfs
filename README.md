# Functionality overview

This is a test page to verify Jekyll + GitHub Pages + GitHub LFS works.

Such setup is unsupported https://github.com/orgs/community/discussions/50337

It does not work out of the box, the LFS resources referenced from GitHub Pages (`![Test Image](/images/test.png)`) give 404.
However, for public repos, there exist a workaround using a Jekyll filter (`![Test Image with a Jekyll filter]({{ '/images/test.png' | lfs_url }})`).

See example at https://marcindulak.github.io/jekyll-github-lfs

# Usage

1. Install Git LFS:
- **macOS:** `brew install git-lfs`
- **Ubuntu/Debian:** `sudo apt-get install -y git-lfs`
- **Windows:** `choco install git-lfs` or download from https://git-lfs.com/

2. Enable Git LFS:
   ```bash
   git lfs install
   ```
   
   This enables Git LFS for image handling.
   Required before pushing images to GitHub.

3. Review [.gitattributes](.gitattributes), and add all files types you want to be stored in GitHub LFS.
Then commit your files normally.

4. Modify [_plugins/lfs_url_filter.rb](_plugins/lfs_url_filter.rb) to hard-code your GitHub username and repo.
   You need to use something like the [build-and-deploy.yml](.github/workflows/build-and-deploy.yml) GitHub Action Workflow for deployment on GitHub Pages, because GitHub Pages ignore custom Jekyll plugins https://github.com/jekyll/jekyll/issues/5265.
   Select "Build and deployment" -> "Source: GitHub Actions" (don't select any action) under your repo settings https://github.com/marcindulak/jekyll-github-lfs/settings/pages, to use the GitHub Action instead.

5. Start Jekyll locally:
   ```bash
   docker run -e REPO_OWNER=marcindulak -e REPO_NAME=jekyll-github-lfs \
          --rm -it -p 127.0.0.1:4000:4000 -v .:/srv/jekyll jekyll/jekyll:3 jekyll serve --verbose
   # Visit http://localhost:4000
   ```
