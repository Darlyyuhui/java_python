﻿
$(function() {
	
	//刷新验证码
	$("#get_code_img").click(function() {		
		$(".getcode").attr("src", "get_code?rand=" + Math.random());
		return false;
	});
	
	//提交
	$("#main_form").submit(function() {
		
		var name = $(".username").val();
		var pwd = $(".password").val();
		var code = $(".Captcha").val();
		console.log("用户信息"+name+"--"+hex_md5(pwd)+"--"+code);
		$.ajax({
			type: "get",
			url: "login?name=" + escape(name) + "&pwd=" + pwd + "&code=" + code,
			dataType: "json",
			
			beforeSend: function() {
				$(".submit_button").attr("disabled", true);
			},
			success: function(data) {
				if(data.code == 0)
					location.href = ""; //登录成功
				else {
					alert(data.desc);
					
					//刷新验证码
					$(".getcode").attr("src", "get_code?rand=" + Math.random());
					$(".Captcha").val("");
				}
			},
			complete: function() {
				$(".submit_button").removeAttr("disabled");
			}
		});

		return false;
	});

});
