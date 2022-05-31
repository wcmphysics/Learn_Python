# Moving a Repository between Gitlab and Github (Mirror and Remote Control)


# Move a repository from A to B (Mirror)

1. Create an empty repository at B.
2. Go to your local repository, and add a remote named `remote_at_B`:

        git remote add remote_at_B ssh_or_https_git_link_at_B.git

3. Push the repository to B:

        git push --mirror remote_at_B

# Remote Control

Note that, after mirroring, branches in your local repository still track the original remote at A, so any push/pull in that branch by default will still be done with A. 

To specify the actual remote to track for each branches, open the file `.git/config`:

    [remote "origin"]
            url = git@A.com:YourUserNameAtA/ssh_or_https_git_link_at_A.git
            fetch = +refs/heads/*:refs/remotes/origin/*
    [branch "master"]
            remote = origin
            merge = refs/heads/master
    [branch "feature_branch"]
            remote = origin
            merge = refs/heads/feature_branch
    [remote "remote_at_B"]
            url = git@B.com:YourUserNameAtB/ssh_or_https_git_link_at_B.git
            fetch = +refs/heads/*:refs/remotes/origin/*

 and change the `remote = ...` under each branch as you wish. 