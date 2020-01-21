
$(document).ready(

		function(){
            $("#favourite").click(function myfun(event){

            	event.preventDefault();//prevents default form submission
                let target= $("#favourite").attr('href');
                console.log(target);
                $.ajax({
                    type : "GET",
                    cache: false,
                    contentType : "application/json",//type of data being send to server
                    url : target,

                    dataType : 'json',//result expected from server
                					//with json return type we can return java objects
                    				//With text we can return String from java conroller
                    timeout : 100000,
                    success : function(data) {
                        console.log(data['status']);
                        if(data['status'] === true)
                    	    $("#star").css("color","gold");
                        else
                            $('#star').css("color","blue");

                    },
                    error : function(e) {
                        console.log("ERROR: ", e);
                    },
                    done : function(e) {
                        console.log("DONE");
                    }
                });
            }
        )
		}

);