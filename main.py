import sublime_plugin
import sublime

# Extends TextCommand so that run() receives a View to modify.
class AddNumbersCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        total = 0 
        # Walk through each region in the selection
        for region in self.view.sel():
            # Get the text of the current region (what's selected)
            #selection = self.view.substr(region)
            # Get a region representing the entire line of the current region (The whole line containing the selection)
            selection = self.view.line(region)
            vals = self.view.substr(selection)
            # Break the selection into multiple values
            vals = vals.split('\n');
            # Add all the values
            for val in vals:
                ints = [int(s) for s in val.split() if s.isdigit()]
                for i in ints:
                    total = total + float(i)
        sublime.message_dialog(str(total))
