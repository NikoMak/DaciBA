//document.getElementById("project").addEventListener("change", () => {
//
//    const project = $("#project :selected").val();
//
//    //alert("sending ajax request!");
//    $.ajax({
//        type: "POST",
//        url: "/tagcloud/ajax_get_topics",
//        data: project, // serializes the form's elements.
//        success: function(data) {
//            console.log(data); // show response.
//        }
//    });
//
////    return false;
//
//});

document.getElementById('project').addEventListener('change', () => {

    //alert("sending ajax request!");
    const request = new XMLHttpRequest();
    request.open('POST', '/tagcloud/ajax_get_topics');

    request.onload = () => {

        const data = JSON.parse(request.responseText);

        if (data.success) {
//            console.log(data.success);
//            console.log(data.topics);
            const topics = JSON.parse(data.topics)
            console.log(topics)

            $("#topic").empty();
            select_topic = document.getElementById("topic");
//            select_topic.empty();

            for(i = 0; i < topics.length; i++){
                const opt = document.createElement('option');
                opt.text = topics[i].topic;
                opt.value = topics[0].id;

                console.log(opt.text);
                console.log(opt.value);
                console.log(select_topic);
                
                select_topic.add(opt);
            }
        }else{
            alert("An error occured while sending the ajax request!");
        }

    }

    const data = new FormData();
    data.append('csrfmiddlewaretoken', csrftoken);
    request.send(data);

    return false;

});
