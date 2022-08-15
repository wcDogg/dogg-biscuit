# External Services

To work with Cookiecutter, you'll need to create several accounts. Most also involve repo-specific steps that happen later in this process.

## PyPy

- Create + verify your [PyPi](https://pypi.org/) account.
- User menu > Account Settings > Generate recovery codes + set up 2FA.
- Account Settings > API Tokens > Add API Token. Copy token to password manager.

Once you have created a project + its GitHub repository:

- GitHub repository > Settings > Secrets > Actions > Add Repository Secret
- Add PyPi token as `PYPI_TOKEN`.

## TestPyPi

- Create + verify your [TestPyPi](https://test.pypi.org/) account.
- User menu > Account Settings > Generate recovery codes + set up 2FA.
- Account Settings > API Tokens > Add API Token. Copy token to password manager.

Once you have created a project + its GitHub repository:

- GitHub repository > Settings > Secrets > Actions > Add Repository Secret
- Add TestPyPi token as `TEST_PYPI_TOKEN`.

## Codecov

- [Sign up using GitHub account](https://codecov.io/).
- Skip the initial 'Which repo are you working with?'.
- Install the [Codecov GitHub App](https://github.com/apps/codecov).
- Then click the Configure button - this takes you to your GitHub account > Applications.
- Review the screen and click Save. Here I set Codecov for specific apps.
- This means moving forward I will have to add repos here manually.

## Read the Docs

- Create + verify your [Read the Docs](https://readthedocs.org) account.
- After verifying, use the Connect with GitHub option.

Once you have created a project + its GitHub repository:

- On the dashboard, import a project + initialize the first build.
- From here it becomes automatic.
