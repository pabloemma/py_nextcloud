
import pycurl
import os
from io import BytesIO
def upload_file(file_path=None, upload_url=None):
        """
        Upload file using curl
        based on https://github.com/Lispython/pycurl/blob/master/examples/file_upload.py
        :param file_path:
        :param upload_url:
        :return: abs file url path of uploaded file.
        """
        if file_path is None or not os.path.exists(file_path):
            print("File '{}' cant be uploaded".format(file_path))
            return

        c = pycurl.Curl()
        # Set curl session option
        c.setopt(pycurl.URL, upload_url)
        c.setopt(pycurl.UPLOAD, 1)
        c.setopt(pycurl.USERPWD,'pabloemma:?Pa!blo?nuke')
        c.setopt(pycurl.READFUNCTION, open(file_path, 'rb').read)
        # Set size of file to be uploaded.
        c.setopt(pycurl.INFILESIZE, os.path.getsize(file_path))

        # c.perform() doesn't return anything,
        # you need to configure a file-like object to capture the value.
        # A BytesIO object would do, you can then call .getvalue() on that
        # after the call completes:
        data = BytesIO()
        c.setopt(c.WRITEFUNCTION, data.write)

        # Start transfer
        print("\nUploading file {} to url {}\n".format(file_path, upload_url))

        # Perform a file transfer.
        c.perform()
        c.close()

        # abs url path of the upload file
        return data.getvalue().decode("UTF-8")


myurl = 'https://www.casitadongaspar.com/nextcloud/remote.php/dav/files/pabloemma/Temperature/'
#myurl = 'https://casitadongaspar.com/nextcloud'
upload_file(file_path = '/Users/klein/login.txt',upload_url=myurl)