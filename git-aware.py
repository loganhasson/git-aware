import sublime, sublime_plugin
import os
import re

class GitAware(sublime_plugin.EventListener):

    # def on_load(self, view):
    #     m = re.search('\A(.*)\/', str(view.file_name()))
    #     # os.chdir(m.group(0))
    #     # cmd = "f="+view.file_name()+"; printf '%s/\\n' \"${f%/*}\""
    #     # os.system("cd "+cmd)
    #     print view.file_name(), os.system("cd"+m.group(0)+"; git symbolic-ref HEAD | sed -e 's,refs/heads/,,'")
  
    # def on_modified(self, view):
    #     m = re.search('\A(.*)\/', str(view.file_name()))
    #     os.chdir(m.group(0))
    #     print view.file_name(), os.system("git symbolic-ref HEAD | sed -e 's,refs/heads/,,'")
  
    # def on_activated(self, view):
    #     m = re.search('\A(.*)\/', str(view.file_name()))
    #     os.chdir(m.group(0))
    #     print view.file_name(), os.system("git symbolic-ref HEAD | sed -e 's,refs/heads/,,'")