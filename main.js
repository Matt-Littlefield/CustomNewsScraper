const { app, BrowserWindow } = require('electron')
const path = require('node:path')

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  mainWindow.loadFile('index.html')

}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})


app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})


// Quits application on close
app.on('window-all-closed', () => {
  app.quit()
})

function getArticleSearch(event) {
  $.ajax({
    type: "POST",
    url: "~/test.py",
    data: { param: text}
  }).done(function( o ) {
     main()
  });
  event.preventDefault();
  keyword = document.getElementById("searchBar").value;
  document.getElementById("demo").innerHTML = keyword;
}