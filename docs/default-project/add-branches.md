# Add Branches

While branching + pull requests are new to me, I've documented large projects where:

- The `main` branch is the production code - the most recent, stable release in distribution.
- There are multiple sprints happening concurrently - features, bug fixes, security updates, and so on.
- Each sprint is on a branch.
- Sprint branches are independently tested then merged to a final staging branch.
- The final deliverable is tested as a whole and released to production as a new version.

In short, branching is how you safely introduce changes into your distributed code. The process is similar when you want to contribute to someone else's project, except you fork instead of branch.

Because I'm new to branching, I'm keeping it simple:

- A `dbot` branch for testing Dependabot PRs + any changes to dependencies.
- A `dev` branch for making + testing changes to code and documentation.

## Create Branch via PowerShell

If you're not already there, `cd` to your project directory and note the prompt indicates you are on the `main` branch. Note we are only adding `dbot` here - `dev` will be added later.

```powershell
# List local branches
git branch

# List remote branches
git branch -r

# Create local + push to GitHub
git branch dbot
git push -u origin dbot

# List open pull requests
gh pr list

# List all pull requests
gh pr list --state "all"

# List pull requests with a label
gh pr list --label "python"
```

## Create Branch via UI

Create a `dbot` branch:

1. Go to the repository's main page.
2. In the upper-left, click the Select Branch menu - it's current label reads `main`.
3. Enter a branch name and click the Create Branch from main option.

## Resources

- GitHub: [About Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- GitHub: [About Branching](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
- noble desktop: [Git Branches](https://www.nobledesktop.com/learn/git/git-branches)
