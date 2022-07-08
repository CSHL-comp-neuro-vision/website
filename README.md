# website

https://cshl-comp-neuro-vision.github.io/website/

## Modifying the source

In the folder `website/source` you will find an `index.rst` file and a set of `.md` files in each subfolder. The markdown files control the content in the build and the index file builds the table of contents.

If you add a new markdown file you need to add a line in the table of contents for it to be included in the site.

## Re-building the site

Clone the repository and run
```
git clone https://github.com/CSHL-comp-neuro-vision/website
conda env create -f environment.yml
```

Every time you need to re-build the HTML files you will need to activate the conda environment and run the make script

```
conda activate sphinx
make html
```

This will place the new build in `build/html`. Copy all of the files in this folder and then switch branches to the `gh-pages` branch. Copy the files into the top-level directory and push to the branch. Return to main before making any changes to the source files.
