# Jono's blog

Here is the source for my blog content.

## eleventy-base-blog v9

A starter repository showing how to build a blog with the [Eleventy](https://www.11ty.dev/) site generator (using the [v3.0 release](https://github.com/11ty/eleventy/releases/tag/v3.0.0)).

## Getting Started

Install dependencies

```
npm install
```

Run Eleventy

Generate a production-ready build to the `_site` folder:

```
npx @11ty/eleventy
```

Or build and host on a local development server:

Visit http://localhost:8080

```
npx @11ty/eleventy --serve
```

Or you can run [debug mode](https://www.11ty.dev/docs/debugging/) to see all the internals.

If deploying to a subdir like on github:

```
npx @11ty/eleventy --pathprefix=blog
```

## Deploy

use git push on the main branch
