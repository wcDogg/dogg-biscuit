## Dependabot Pull Requests

**IMPORTANT:** This topic is a hot mess - I need to learn about resolving GitHub merge conflicts with `poetry.lock`.

The big idea is that over time, Dependabot is going to help manage project dependencies by automatically submitting PRs for each update.

When you first add the `dependabot.yml`, you'll often get several PRs within just a few minutes. **This topic is about dealing with the initial wave of version update PRs - vs security PRs which require extra steps to merge with `dbot`.**

In later steps we are going to test the `main` branch which has an unaltered Cookiecutter project. Then test the `dbot` branch with version updates to ensure nothing breaks. Then merge these updates back to `main`.

Moving forward, you'll need to monitor and decide how often to repeat this process.

## About Dependabot PRs

- A single pull request has a single branch - and vice-versa.
- Dependabot creates a PR + branch for each dependency that needs updating.
- Once merged, Dependabot deletes the branch.
- When you merge, there are 3 options [described here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges).

## Merge Dependabot Branches

This step merges each Dependabot version update PR to the `dbot` branch. This can be done in PowerShell, but is best done via the GUI.

My first wave had 16 Dependabot PRs - fair warning, this took several hours to complete.

**IMPORTANT:** I know from past experience that order can matter when changing things. Still, I had to learn the hard way that it matters here. Address PRs in order, starting from #1. Allow time for tests to finish between merges.

1. Go to the repository's Pull Requests tab.
2. Notice each PR has a green check mark indicating it has passed all tests and there are no conflicts.
3. Click a request's title to view details.
4. If the request indicates there are still tests in progress and the Merge Pull Request button is NOT green, then wait for tests to finish. The screen should refresh automatically.
5. Once green, click the Merge Pull Request button.
6. Click the Confirm Merge button.
7. Return to the Pull Requests tab and repeat for each PR.

Between merges, you'll notice that previously green check marks will change.

- A yellow dot means there are tests in progress - You just need to wait for these to finish.
- A red X means a test failed. This is okay as long as it's got other PRs in front of it, which will likely resolve the failure.

## Resolve Conflict with poetry.lock

During this wave, my last 4 PRs could not be merged due to a conflict with `poetry.lock`. At this point we haven't touched Poetry, but I did notice `dependabot.yml` has an ecosystem where `versioning-strategy: lockfile-only` - this has to be related, right?

TODO: This section is on hold until I learn how to resolve these conflicts.

- https://cookiecutter-hypermodern-python.readthedocs.io/en/2022.6.3.post1/guide.html#version-constraints
- https://github.com/python-poetry/poetry/issues/496
- https://python-poetry.org/docs/basic-usage/#updating-dependencies-to-their-latest-versions
- https://cookiecutter-hypermodern-python.readthedocs.io/en/2022.6.3.post1/guide.html#dependabot

Dependencies in the Hypermodern Python Cookiecutter are managed by Dependabot. When newer versions of dependencies become available, Dependabot updates the poetry.lock file and submits a pull request.

## References

- https://www.youtube.com/watch?v=Q1kHG842HoI
