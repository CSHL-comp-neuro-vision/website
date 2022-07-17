# Script to push html doc files to gh pages
make html

# Repo information
ORG=CSHL-comp-neuro-vision
REPO=website

mkdir ~/temp/
# Copy the build folder into a temp folder
cp -R ./build/html/* ~/temp/

# Clone the gh-pages branch to local documentation directory
git clone -b gh-pages "https://github.com/$ORG/$REPO.git" gh-pages
cd gh-pages

# Copy everything from temp into gh-pages branch
cp -R ~/temp/* ./

# Add and commit all changes
git add -A .
git commit -m "$1 commit";

# Push the changes
git push -q origin gh-pages

# Leave gh-pages repo and delete
cd ../
rm -rf gh-pages





