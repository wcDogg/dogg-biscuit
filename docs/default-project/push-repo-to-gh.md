# Push Repository to GitHub

At this point we have created a Cookiecutter project, initialized a local repository, performed a `poetry update`, and have ran all Nox tests. The next step is to push the local repository to GitHub

## IMPORTANT: Stash dependabot.yaml

Before creating the repository, move `.github/dependabot.yml` into a temp location outside the project directory and commit the change. Later, we create a branch for Dependabot to submit PRs to. You can't add this file before creating the branch.

```powershell
git add . && git commit -m "Stashed dependabot.yml"
```

## Create Repository

```powershell
gh repo create

# Follow the prompts, answers are as follows:

? What would you like to do? Push an existing local repository to GitHub
? Path to local repository .
? Repository name dogg-biscuit
? Description A description here
? Visibility Public
? Add a remote? Yes
? What should the new remote be called? origin
? Would you like to push commits from the current branch to "origin"? Yes
```

## Add Tokens

See: [External Services](external-services.md)

- GitHub > Repository > Settings > Secrets > Actions > Add New Repository Secret
- Add the `PYPI_TOKEN` and `TEST_PYPI_TOKEN` generated when you created these accounts.

## Add Codecov

When I installed [Codecov](../environment/external-services.md/#codecov) on my GitHub account, I configured it for specific repositories vs all.

- GitHub > User menu > Settings > Applications > Codecov > Add repo

## Review the Initial Commit

Go to the repository's Actions tab - there are a series of workflows that were executed when the repo was created.

All workflows should succeed except the Release workflow. This happens because the PyPi tokens weren't available at the time. Now they are and we can rerun the test to confirm.

1. Click the failed workflow's title - 'Initial Commit'.
2. In the left panel, hover over the Release job and click its re-run icon.
3. Review the message and click Re-run Jobs.
4. Wait for tests to complete - all jobs should pass.
