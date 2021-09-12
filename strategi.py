instrument{ name = "China r1zco",
				short_name = "EC",
				icon = "https://lh3.googleusercontent.com/a-/AOh14GhOMw-SBEHKf4dvwmVgwxUJaendPKluwo0itoR2MQ=s600-k-no-rp-mo",
				overlay = true }
				
input_group ( "CALL", call_color = input( defaut = "green", type = input.color ) )
input_group ( "PUT", call_color = input( defaut = "red", type = input.color ) )

ssma_3 = ssma(close, 3)
ssma_50 = ssma(close, 50)

MovAvarDev = ssma(close, 20)
MovAvarDev = close - MovAvarDev

drop_plot_value("PUT", current_bar_id)
drop_plot_value("CALL", current_bar_id)

plot_shape( (ssma_3 >= ssma_50 and ssma_3[1] < ssma_50[1] and ssma_3[2] < ssma_50[2] and MovAvarDev > MovAvarDev[1]),
			"CALL",
			shape,style.arrowup,
			shape_size.huge,
			call.color,
			shape_location.belowbar,
			0,
			"CALL",
			call_color)
			
			
plot_shape( (ssma_3 <= ssma_50 and ssma_3[1] > ssma_50[1] and ssma_3[2] > ssma_50[2] and MovAvarDev < MovAvarDev[1]),
			"PUT",
			shape_style.arrowdown,
			shape_size.huge,
			put_color,
			shape_location.abovebar,
			0,
			"PUT",
			put_color)
