function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");

		if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);

            if (c_end == -1)
				c_end = document.cookie.length;

            return unescape(document.cookie.substring(c_start,c_end));
        }
    }

    return "";
}

$(document).ready( function()
{
	$.ajaxSetup(
	{
		headers: { "X-CSRFToken": getCookie("csrftoken") }
	});

	$.ajax(
	{
		url : "/blog/get_subjects/",
		type : "POST",
		success : function(json)
		{
			$.each(json.subjects, function (i, value)
			{
				$("#subject-menu").append("<a class='dropdown-item' href='" + value.url + "'>" + value.title + "</a>");
			});
		}
	});
});