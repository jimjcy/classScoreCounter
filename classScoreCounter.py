# -*- coding: utf-8 -*-
import lib.frames as frames
import lib.util as util

if __name__ == '__main__':
    initFolderLogger = util.rootLogger.getChild("initFolder")
    if util.initFolder() == False:
        initFolderLogger.error("The folder is not initialized, creating the folder and files")
        frames.createFileWindow().mainloop()
        initFolderLogger.info("The folder is initialized.")
    else:
        initFolderLogger.info("The folder is initialized.")
    window = frames.initWindow()
    frames.mainFrame(window)
    window.mainloop()