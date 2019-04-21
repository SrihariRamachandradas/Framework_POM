import win32com.client
control = win32com.client.Dispatch('HttpWatch.Controller')
plugin = control.Chrome.new()

plugin.Log.EnableFilter(False)
plugin.Clear()
plugin.clearCache
plugin.Record()
plugin.GotoURL("http://localhost/login.do")
control.Wait(plugin, -1)
plugin.Stop()
print(plugin.Log.entries.count)

for s in plugin.Log.entries:
    print(s.URL)
    print(s.time)
    print('code:' + str(s.result))
Entries = plugin.Log.Pages.Item(0).Entries
summary = Entries.summary
print("Total time to load page(secs):",summary.Time)
