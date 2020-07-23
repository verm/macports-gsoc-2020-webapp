$(function () {
    const macports_packages = ['10_12', '10_13', '10_14', '10_15'];

    function getOsVersion() {
        let userAgent = navigator.userAgent.toLowerCase();

        for (let i = 0; i < macports_packages.length; i++) {
            let version = macports_packages[i];
            let matchString = `mac os x ${version}`;
            if (userAgent.search(matchString) !== -1) {
                return version;
            }
        }

        return false;
    }

    const osVersion = getOsVersion();
    if(osVersion) {
        $("#download-instructions").html(`Download MacPorts for your MacOS ${osVersion.replace('_', '.')}`);
    } else {
        $("#download-instructions").html(`Download MacPorts`);
    }
});