import typer
import os
import time
from githubclass import Github
from typing import Optional

def main(name: str, gith: Optional[str] ) -> str:
  typer.secho('Creating Your Project! 📦', fg=typer.colors.BRIGHT_MAGENTA, bold=True)
  cuf = os.getcwd()
  os.mkdir(name)
  pro_file = cuf + f'/{name}'
  time.sleep(1)
  os.chdir(pro_file)
  time.sleep(1)
  os.system('touch Readme.md')
  time.sleep(3)
  os.system('git init')
  os.system('git add .')
  os.system('git commit -m "Initial Commit"')

  try:
    if gith == 'github':
      usern = typer.prompt('Username')
      passwd = typer.prompt('Password', hide_input=True)
      choice = typer.prompt('Private/Public')
      github = Github(usern, passwd, choice, name)
      github.login()

      if github.login():
        os.system(f"git remote add origin git@github.com:{usern}/{name}.git")
        time.sleep(1)
        os.system("git branch -M main")
        time.sleep(1)
        os.system("git push -u origin main")
        typer.secho(f'Projecet Created at {pro_file}', fg=typer.colors.BRIGHT_GREEN)
        typer.secho(f'Github Repo: https://github.com/{usern}/{name}', fg=typer.colors.BRIGHT_GREEN)
        return "Logged In"

      else:
        typer.secho('Unable To Log In')


    else:
      typer.secho(f'Project Created at {pro_file}', fg=typer.colors.BRIGHT_GREEN)
      return "Created Project Without Github Repo!"
  
  except:
    os.rmdir(f'{name}')
    typer.secho('Unable To Create Project!', fg=typer.colors.RED)
    return "Invalid Credentials!"
    
if __name__=="__main__":
  typer.run(main)