def runfzf(tech):
    """Runs FZF Selection Prompt
    Takes a list or dictionary of items and returns single string"""
    from pyfzf.pyfzf import FzfPrompt

    fzf = FzfPrompt()
    choice = fzf.prompt(tech)
    return choice[0]


def choose(tech):
    """Choose the Framework to be setup"""

    lang = runfzf(tech)
    choice = runfzf(tech[lang])
    func = tech[lang][choice]

    return func, lang, choice
