#!/bin/bash

# Define the path to your GitHub repository
REPO_PATH="/path/to/your/repository"

# Change directory to the repository
cd $REPO_PATH

# Get the list of files in the repository
FILES=$(ls)

# Counter for the number of committed files
COMMIT_COUNT=0

# Function to generate a commit message
generate_commit_message() {
    local FILE_NAME="$1"
    local COMMON_WORDS=("edited" "updated" "modified" "fixed" "added")

    # Choose a random common word
    local RANDOM_WORD=${COMMON_WORDS[$RANDOM % ${#COMMON_WORDS[@]}]}

    # Create the commit message
    echo "$RANDOM_WORD $FILE_NAME"
}

# Loop through each file in the repository
for FILE in $FILES; do
    # Check if the file contains the word "main"
    if [[ $FILE == *"main"* ]]; then
        echo "Skipping file with 'main' in its name: $FILE"
    else
        # Add the file
        git add "$FILE"

        # Generate a commit message
        COMMIT_MESSAGE=$(generate_commit_message "$FILE")

        # Commit the changes
        git commit -m "$COMMIT_MESSAGE"

        # Increment the commit count
        ((COMMIT_COUNT++))
    fi
done

# Display the number of committed files
echo "Number of files committed: $COMMIT_COUNT"

# Push changes to the remote repository
git push origin master
