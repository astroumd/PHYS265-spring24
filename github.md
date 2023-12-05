# git and github

**git** is arguably the most common Version Control System on the market, and
very popular with Open Source Software. https://github.com is one of the major
contenders, although gitlab and bitbucket offer competative interfaces to
maintain your git repository.

In this class you will learn how to use github to maintain a repository, but if you
already use another host, feel free to use it.

If these terms makes sense to you, we will not use git branches, or learn how to submit
a pull request. These will be available for extra credit though.


## Authentication

As of 2024 github will enforce 2FA (two-factor authentication). Although you will find
everything you need to know to work with github on their website, there are numerous
web pages summarizing this. One example is on https://swcarpentry.github.io/git-novice/ which
covers the all important
[*Installing Git*](https://swcarpentry.github.io/git-novice/#installing-git)
and
[*Creating a GitHub Account*](https://swcarpentry.github.io/git-novice/#creating-a-github-account)
to get your started on Linux, Mac, or Windows.

There are two methods how to automate your authentication with github:

### 1. Personal Access Tokens

Settings -> Developer Setting  -> Personal access tokens -> Tokens (classic) -> generate new token

https://github.com/settings/tokens

Typically you will get a token, something like

      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

that you will then use as a password. When it was generated, you also had to give oit a lifetime. Pick one year.

### 2. SSH keys

Settings -> SSH and GPG keys -> new SSH key

https://github.com/settings/keys


## Class Repository

You actually don't need a github account to get a public repository, e.g.

      git clone https://github.com/astroumd/PHYS265-spring24

or if you have setup your git using ssh keys

      git clone git@github.com:astroumd/PHYS265-spring24.git


