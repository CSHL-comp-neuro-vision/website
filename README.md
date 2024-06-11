# website

https://cshl-comp-neuro-vision.github.io/website/

## Basic info
The github repo for the website lives here: https://github.com/CSHL-comp-neuro-vision/website

The website lives here: https://cshl-comp-neuro-vision.github.io/website/

## Gaining access
* Add new members here: https://github.com/orgs/CSHL-comp-neuro-vision/people
* You can only added by other owners. Ask them to add you by your github account name.
	* TAs and organizers are added as "owners" (more privileges)
	* Students are "members" (less privileges)
* Add and organize year-specific team-members: https://github.com/orgs/CSHL-comp-neuro-vision/teams 
	* TAs and organizers are in "organizers-XX" teams (XX = last two digits of year)
	* Students and TAs are in "students-XX" teams (XX = last two digits of year)


## General website structure
There are two branches:
* "main" 		: Place where you actively modify things / add markdown and paper pdf files.
* "gh-pages" 	: Where the website technically lives (you only update new versions of html files, you do NOT directly edit here).

In the folder `website/source` you will find an `index.rst` file and a set of markdown (.md) files in subfolders. The markdown files control the website content and the index file builds the table of contents. If you add a **new** markdown file, you need to add a line in the table of contents for the page to be included in the site (including `index.rst` file (and maybe other places?))

There is also a separate "slides-2024" repository. This is a private repository where the lecture slides live. This is separate repo to avoid pushing/pulling large files to the website (we _think_). We create hyperlinks to these pdfs when adding lecture notes in the markdown files of the "main" website branch repo.


## General repository organization
- website/
	- `source` 						: second most important folder!
	- `_static`  					: folder with static files
		- course_projects 				: pdfs of projects that turned into actual papers
		- images 						: profile pictures, etc.
		- pdfs 							: pdfs linked to suggested readings markdown page
		- t-shirts 						: jpegs of previous course t-shirts
	- `2022` (-- obsolete folder kept for reference, soon will be deleted)
	- `2024`  						: most important folder!
		- course_tshirt_submissions.md  : Page with instructions to submit t-shirt submissions (and inspirations from prior years)
		- lecture_notes.md 				: Page with lecture slides and suggested readings (pdfs).
		- people.md 					: Page with 2024 Organizers, TAs and students 
		- photos.md 					: Page with URL to Google Photo album
		- project_ideas.md 				: Page with URL to suggested project ideas by lecturers
		- schedule.md 					: Page with schedule
	- `past`
		- build_markdown.py 			: script to build "output.md" and "past courses.md"
		- remove_duplicate_websites.py 	: script to clean up "websites.csv"
		- websites.csv 					: information about past lecturers
		- websites_no_duplicates.csv 	: you guessed it
		- participants.json 			: former students, lecturers, organizers
		- output.md 					: general config file, built by build_markdown.py
		- past_courses.md 				: general config file, built by build_markdown.py
		- tutorials 					: Markdown file to add code tutorials. Note: most of them are on github so this page is kind of obsolete.
	- `index.rst` 						: Configuration file for main page, overall website tree, static pages.
	- `conf.py` 							: Configuration file for website builder (shouldn't change, except for updating project information once)  
		
	- `build` 						: Output folder of run "make html" with sphinx toolbox, i.e. html files for website.
	- `_build` (-- not sure, contents seem ignored?)
	- `_source` (-- not sure, contents seem ignored?)


## How do I add materials?

### Step 0: First time setting up website repo on your local machine

1. Clone/set up website repo on your local machine

```
git clone https://github.com/CSHL-comp-neuro-vision/website
conda env create -f environment.yml
```

2. Checkout the "main" branch

```
git checkout main
```

## Step 1: Modifying the source ("main" branch)

In the folder `website/source` you will find an `index.rst` file and a set of `.md` files in each subfolder. The markdown files control the content in the build and the index file builds the table of contents.

If you add a new markdown file you need to add a line in the table of contents for it to be included in the site.

***NOTE: Every time before you want to make changes to "main" branch, always first pull "main" branch to check for updates***

``` 
git pull origin main
```

### A. Lecture slides (pdfs stored in the "slide-2024" repo).
1. Make a folder with the Lecturer's last name
2. Add pdfs
3. Push changes to git repo
4. Link pdfs to Lecturer's section in "main" branch ../website/source/2024/lecture_notes.md to full repository URL with html "href" command: `<a href= "https://github.com/CSHL-comp-neuro-vision/slides-2024/raw/main/<last_name>/<file_name.pdf>" Slides part X </a>`
5. Update website (see Step 2: Re-building the site)

### B. Suggested readings (suggest_readings.md + pdfs)
1. Add pdfs to static/pdf folder
2. Open `../website/source/2024/lecture_notes.md`
3. Link pdfs to text in `lecture_notes.md` markdown file. 
4. Update website (seeStep 2: Re-building the site)

### C. Suggested project ideas (also suggest_readings.md)  
1. Add pdfs to `website/source/_static/pdfs/` folder
2. Open `lecture_notes.md` markdown file, link pdfs to text, for example:
`<a href="../_static/pdfs/cohen/rust_cohen_2022.pdf">Rust & Cohen (2022)</a>`
3. Update website (see Step 2: Re-building the site)

### D. Schedule (schedule.md) has links to Lecturer's lecture_notes.md  
1. Open `website/source/2024/lecture_notes.md`,
2. Update text and make links (like step 2 of "suggested project ideas")
3. Update website (see Step 2: Re-building the site)



## Step 2: Re-building the site

1. Now you made changes to markdown files and/or added pdfs as static files, you want to add changes to the git server

```
git add <file1> <file2> <file3> … 
git commit -am '[leave a comment here]'
git push origin main
```

2. Every time you need to re-build the HTML files you will need to activate the conda environment and run the `make` script (while you STAY on the "main" branch):

```
conda activate sphinx
make html
```

This will place the new build in `build/html`. 

3. Go to folder in Finder: Copy all of the files from the build/html folder. 
(EK: we should make an automated bash script for this. Or maybe we can do this with git? `E.g.: git diff <other-branch-name> -- <filename> ` or `git hash-object`).

4. Go to Terminal: Switch branches from "main" to the `gh-pages` branch (again, first pull for any changes). 
```
git checkout gh-pages
git pull origin gh-pages
```

4. Copy the files into the top-level directory and push to the branch. (i.e., check the changed files and add them to the server 

```
git diff
git add <file1> <file2> <file3> … 
git commit -am '[leave a comment here]'
git push origin gh-pages
```

5. Return to "main" branch before making any changes to the source files.

```
git checkout main and push to the branch. 

```








