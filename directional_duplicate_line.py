import sublime, sublime_plugin

class DirectionalDuplicateLineCommand(sublime_plugin.TextCommand):
    """
        Duplicate line/selection before or after the current one. As it turns out, 
        duplicating "before" just means restoring each selection to the state it was
        before duplication.
    """
    def run(self, edit, direction=0):
        self.oldSelections = []

        if direction: # before
            self.duplicate(edit, True)
        else: # after
            self.duplicate(edit)

    def duplicate(self, edit, restoreSelections=False):
        self.view.run_command("expand_selection", {"to": "line"})
        for region in self.view.sel():
            self.oldSelections.append(sublime.Region(region.begin(), region.end()))
            if region.empty():
                line = self.view.line(region)
                line_contents = self.view.substr(line) + '\n'
                self.view.insert(edit, line.begin(), line_contents)
            else:
                self.view.insert(edit, region.begin(), self.view.substr(region))
        
        if restoreSelections:
            self.view.sel().clear()
            for region in self.oldSelections:
                self.view.sel().add(region)
        
