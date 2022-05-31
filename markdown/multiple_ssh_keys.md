# Create SSH Connections for Gitlab and Github on the Same Windows Machine

The content is mainly from [this tutorial](https://medium.com/@viviennediegoencarnacion/manage-github-and-gitlab-accounts-on-single-machine-with-ssh-keys-on-mac-43fda49b7c8d) and [ssh trouble shooting](https://stackoverflow.com/questions/17846529/could-not-open-a-connection-to-your-authentication-agent).

All the commands have been tested on Git Bash for Windows. 


1. Create ssh Keys

        ssh-keygen -t rsa -C "personal@mail.com" -f ~/.ssh/id_rsa_gitlab
        ssh-keygen -t rsa -C "personal@mail.com" -f ~/.ssh/id_rsa_github

2. Register the Keys on Github and Gitlab

    - Github: copy public key in `id_rsa_github.pub` -> setting -> SSH and GPG keys -> new SSH key
    - Gitlab: copy public key in `id_rsa_gitlab.pub` -> preference -> SSH keys -> add key

3. Register the Keys on the Local Machine

    - Activate ssh-agent by:

            eval `ssh-agent -s`
    
    - Add the keys:
    
            ssh-add ~/.ssh/id_rsa_github
            ssh-add ~/.ssh/id_rsa_gitlab
    

4. Create/Edit the Config File as the following:

        # Github account
        Host github.com
            HostName github.com
            User YourAccountName
            IdentityFile ~/.ssh/id_rsa_github

        # Gitlab account
        Host gitlab.com
            HostName gitlab.com
            User YourAccountName
            IdentityFile ~/.ssh/id_rsa_gitlab

5. Done!


