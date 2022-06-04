import time
import typer
import requests

ls = ['fnsd', "afdsf", "fdsfsd"]
with typer.progressbar(ls) as prog:
  for i in ls:
    print(i)
