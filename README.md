# ionos-dns-python

[![Release](https://img.shields.io/github/v/release/FredStober/ionos-dns-python)](https://img.shields.io/github/v/release/FredStober/ionos-dns-python)
[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/ionos-dns-python/Main/main)](https://github.com/fpgmaas/ionos-dns-python/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/FredStober/ionos-dns-python/branch/main/graph/badge.svg)](https://codecov.io/gh/FredStober/ionos-dns-python)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FredStober/ionos-dns-python)](https://img.shields.io/github/commit-activity/m/FredStober/ionos-dns-python)
[![License](https://img.shields.io/github/license/FredStober/ionos-dns-python)](https://img.shields.io/github/license/FredStober/ionos-dns-python)

This contains tools to use the IONOS DNS management API in oder to perform letsencrypt DNS challenges

- **Github repository**: <https://github.com/FredStober/ionos-dns-python/>
- **Documentation** <https://FredStober.github.io/ionos-dns-python/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:FredStober/ionos-dns-python.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with 

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting 
[this page](https://github.com/FredStober/ionos-dns-python/settings/secrets/actions/new).
- Create a [new release](https://github.com/FredStober/ionos-dns-python/releases/new) on Github. 
Create a new tag in the form ``*.*.*``.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).