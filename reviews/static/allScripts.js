function goToPage(pageNumber) {
    var url = window.location.href;
    if (window.location.href.indexOf("?") !== -1) {
        //if we are already paginated
        // Replace the last character with the pageNumber argument
        newUrl = url.substring(0, url.length - 1) + pageNumber;
    }
    else {
        newUrl = url + "?page=" + pageNumber;
    }
    // Go to the new URL
    window.location.href = newUrl;
    }

    function goToDetails(newUrl) {
        window.location.href = newUrl;
    }
