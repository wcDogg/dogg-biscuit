# Configure Dependabot

Dependabot is a GitHub service that monitors a repository's code. Dependabot helps manage dependencies in 2 ways:

- Dependency version updates - These are configured in the project's `.github/dependabot.yaml` and can be targeted at the `dbot` branch.
- Security vulnerability updates - These are configured in the GitHub UI per repo. With the right configuration, we can receive alerts and manually create PRs on `dbot`.

**IMPORTANT:** Be sure the `dbot` [branch exists](add-branches.md).

## Version Updates

### Edit dependabot.yml

We previously stashed `dependabot.yml` outside the project directory. Restore it to the `.github` directory and add `target-branch: "dbot"` to each ecosystem:

```
version: 2
updates:
  - package-ecosystem: github-actions
    directory: "/"
    target-branch: "dbot"
    schedule:
      interval: daily
  - package-ecosystem: pip
    directory: "/.github/workflows"
    target-branch: "dbot"
    schedule:
      interval: daily
  - package-ecosystem: pip
    directory: "/docs"
    target-branch: "dbot"
    schedule:
      interval: daily
  - package-ecosystem: pip
    directory: "/"
    target-branch: "dbot"
    schedule:
      interval: daily
    versioning-strategy: lockfile-only
    allow:
      - dependency-type: "all"
```

### Commit to the main Branch

Commit `dependabot.yml` to `main`. Within a few minutes you will probably see several PRs. Hover over a request and notice they are for the `dobot` branch

```powerhsell
git add . && git commit -m "Add Dependabot version updates"
git push
```

### Update the dbot Branch

In GitHub, switch to the `dobot` branch and notice there is a message advising the `dbot` branch is 1 commit behind `main` - this is the `dependabot.yml`.

It's common for changes to happen on `main` while working on another branch. Typically, you want to test a branch against the most recent version of `main`. Here's a simple merge to update `dbot` from `main`:

```powershell
# Switch to the dbot branch
git switch dbot

# Merge + push
git merge main -m "Update from main"
git push
```

Go to the repository and switch to the `dbot` branch. Notice the messaging is gone and the `.github` directory now contains `dependabot.yml`.

## Security Vulnerabilities

To enable Dependabot for security vulnerabilities:

1. Repository > Security tab
2. Enable Security Advisories
3. Enable Dependabot Alerts - a Configuration screen opens
   1. Enable Dependabot Alerts - we need manual control to send PR to `dbot`.
   2. DO NOT enable Dependabot Security Updates - this sends PRs to `main`.

## Resources

- GitHub: [Dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates)
- GitHub: [Dependabot Version Updates](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#ignore)
- Youtube: [GitHub Tutorial: Dependabot Basics](https://www.youtube.com/watch?v=8WaYbeOSCoE)
