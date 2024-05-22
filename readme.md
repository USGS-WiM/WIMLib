<a href="https://wim.usgs.gov/#/">
	<span><img src="https://wim.usgs.gov/visuals/branding/wimvector.png">Web Informatics and Mapping</span>
</a>
<br>

Update, 2024-05-22: Deprecated

This repository has been has moved to a different hosting platform and is no longer being actively maintained. Please see https://code.usgs.gov/WiM/wimlib (USGS internal access may be required) for latest updates related to this effort.

# Summary
WiMPy is a custom reusable libraries and objects for handling geojson, logging, and spatial operations leveraging ESRI ArGIS.

## Requirements

### ArcGIS 10.x
* You will be using ESRI's ArcGIS ArcPy library for geoprocessing. If you have not installed ArcGIS before, you can skip to the next section.
* If you already have ArcGIS installed on your machine, then you might need to reinstall it. If you are reinstalling, delete C:\Python27 and C:\Program Files (x86)\ArcGIS to remove the files from your machine. Once that is done, download ArGIS from your favorite repository or have an IT administrator add it to your machine. During installation, if you are prompted to overwrite a file, choose the option to overwrite as it will help you clean up your installation (i.e. miscellaneous parts that ESRI has a tendency of leaving out and about on your computer).
* Following installation, verify that you have Python up and working correctly. Open ArcMap or ArcCatalog to verify the installation worked as expected. 

### Set Python as a System Variable
* Go to the Start Menu
* Right click on _Computer_
* Select _Properties_
* Select _Advanced Systems Settings_
* Click _Environment Variables_
* Under _System Variables_, find _Path_ and press _Edit_
* Add `C:\Python27\ArcGIS10.3` or whatever your relevant path is.
* Click _OK_
* Click _OK_, again
* Open the Command Prompt and type `python` which should turn your Command Prompt into a Python Command Prompt allowing you to use Python commands. It is useful to also obtain the version using `python --version` from the command line. If you're using ArcGIS 10.3.1 you should have Python 2.7.8.

### Pip and Related Packages
* Go [here](https://pip.pypa.io/en/stable/installing/), open the get-pip.py file and save it to your computer. Personally, I open a copy of Notepad++ and save the file.
* Open the Command Prompt, navigate to where get-pip.py is and execute the command `python get-pip.py` this will download and install Pip.
* Install requests, cirtifi, and virtualenv by executing `pip install requests` `pip install cirtifi` `pip install virtualenv`

### netCDF
* For Windows
* Download and install HD5 1.8.18 from [here]
(https://support.hdfgroup.org/HDF5/).
* Make an environmental variable HDF5_DIR that's value is the installation directory of HDF5.
* Download and install netCDF 4.4.1.1 from [here]
(https://www.unidata.ucar.edu/downloads/netcdf/index.jsp
* Make an environmental variable NETCDF4_DIR that's value is the installation directory of netCDF4.
* Download and pip install the appropriate netCDF4 wheel file from [here] (http://www.lfd.uci.edu/~gohlke/pythonlibs/)

* For Linux
* Use the distribution's respective package manager to install HDF5 and netCDF4.  Then use pip to install netCDF4 for Python.

