@ stdcall wined3d_mutex_lock()
@ stdcall wined3d_mutex_unlock()

@ cdecl wined3d_check_depth_stencil_match(ptr long long long long long)
@ cdecl wined3d_check_device_format(ptr long long long long long long long)
@ cdecl wined3d_check_device_format_conversion(ptr long long long long)
@ cdecl wined3d_check_device_multisample_type(ptr long long long long long ptr)
@ cdecl wined3d_check_device_type(ptr long long long long long)
@ cdecl wined3d_create(long ptr)
@ cdecl wined3d_decref(ptr)
@ cdecl wined3d_enum_adapter_modes(ptr long long long ptr)
@ cdecl wined3d_get_adapter_count(ptr)
@ cdecl wined3d_get_adapter_display_mode(ptr long ptr)
@ cdecl wined3d_get_adapter_identifier(ptr long long ptr)
@ cdecl wined3d_get_adapter_mode_count(ptr long long)
@ cdecl wined3d_get_adapter_monitor(ptr long)
@ cdecl wined3d_get_device_caps(ptr long long ptr)
@ cdecl wined3d_get_parent(ptr)
@ cdecl wined3d_incref(ptr)
@ cdecl wined3d_register_software_device(ptr ptr)

@ cdecl wined3d_buffer_create(ptr ptr ptr ptr ptr ptr)
@ cdecl wined3d_buffer_create_ib(ptr long long long ptr ptr ptr)
@ cdecl wined3d_buffer_create_vb(ptr long long long ptr ptr ptr)
@ cdecl wined3d_buffer_decref(ptr)
@ cdecl wined3d_buffer_free_private_data(ptr ptr)
@ cdecl wined3d_buffer_get_parent(ptr)
@ cdecl wined3d_buffer_get_priority(ptr)
@ cdecl wined3d_buffer_get_private_data(ptr ptr ptr ptr)
@ cdecl wined3d_buffer_get_resource(ptr)
@ cdecl wined3d_buffer_incref(ptr)
@ cdecl wined3d_buffer_map(ptr long long ptr long)
@ cdecl wined3d_buffer_preload(ptr)
@ cdecl wined3d_buffer_set_priority(ptr long)
@ cdecl wined3d_buffer_set_private_data(ptr ptr ptr long long)
@ cdecl wined3d_buffer_unmap(ptr)

@ cdecl wined3d_clipper_create()
@ cdecl wined3d_clipper_decref(ptr)
@ cdecl wined3d_clipper_get_clip_list(ptr ptr ptr ptr)
@ cdecl wined3d_clipper_get_window(ptr ptr)
@ cdecl wined3d_clipper_incref(ptr)
@ cdecl wined3d_clipper_is_clip_list_changed(ptr ptr)
@ cdecl wined3d_clipper_set_clip_list(ptr ptr long)
@ cdecl wined3d_clipper_set_window(ptr long ptr)

@ cdecl wined3d_device_acquire_focus_window(ptr ptr)
@ cdecl wined3d_device_begin_scene(ptr)
@ cdecl wined3d_device_begin_stateblock(ptr)
@ cdecl wined3d_device_clear(ptr long ptr long long float long)
@ cdecl wined3d_device_clear_rendertarget_view(ptr ptr ptr)
@ cdecl wined3d_device_color_fill(ptr ptr ptr ptr)
@ cdecl wined3d_device_create(ptr long long ptr long ptr ptr)
@ cdecl wined3d_device_decref(ptr)
@ cdecl wined3d_device_delete_patch(ptr long)
@ cdecl wined3d_device_draw_indexed_primitive(ptr long long)
@ cdecl wined3d_device_draw_indexed_primitive_strided(ptr long ptr long ptr long)
@ cdecl wined3d_device_draw_indexed_primitive_up(ptr long ptr long ptr long)
@ cdecl wined3d_device_draw_primitive(ptr long long)
@ cdecl wined3d_device_draw_primitive_strided(ptr long ptr)
@ cdecl wined3d_device_draw_primitive_up(ptr long ptr long)
@ cdecl wined3d_device_draw_rect_patch(ptr long ptr ptr)
@ cdecl wined3d_device_draw_tri_patch(ptr long ptr ptr)
@ cdecl wined3d_device_end_scene(ptr)
@ cdecl wined3d_device_end_stateblock(ptr ptr)
@ cdecl wined3d_device_enum_resources(ptr ptr ptr)
@ cdecl wined3d_device_evict_managed_resources(ptr)
@ cdecl wined3d_device_get_available_texture_mem(ptr)
@ cdecl wined3d_device_get_back_buffer(ptr long long long ptr)
@ cdecl wined3d_device_get_base_vertex_index(ptr)
@ cdecl wined3d_device_get_clip_plane(ptr long ptr)
@ cdecl wined3d_device_get_clip_status(ptr ptr)
@ cdecl wined3d_device_get_creation_parameters(ptr ptr)
@ cdecl wined3d_device_get_current_texture_palette(ptr ptr)
@ cdecl wined3d_device_get_depth_stencil(ptr ptr)
@ cdecl wined3d_device_get_device_caps(ptr ptr)
@ cdecl wined3d_device_get_display_mode(ptr long ptr)
@ cdecl wined3d_device_get_front_buffer_data(ptr long ptr)
@ cdecl wined3d_device_get_gamma_ramp(ptr long ptr)
@ cdecl wined3d_device_get_index_buffer(ptr ptr)
@ cdecl wined3d_device_get_light(ptr long ptr)
@ cdecl wined3d_device_get_light_enable(ptr long ptr)
@ cdecl wined3d_device_get_material(ptr ptr)
@ cdecl wined3d_device_get_npatch_mode(ptr)
@ cdecl wined3d_device_get_palette_entries(ptr long ptr)
@ cdecl wined3d_device_get_pixel_shader(ptr)
@ cdecl wined3d_device_get_primitive_type(ptr ptr)
@ cdecl wined3d_device_get_ps_consts_b(ptr long ptr long)
@ cdecl wined3d_device_get_ps_consts_f(ptr long ptr long)
@ cdecl wined3d_device_get_ps_consts_i(ptr long ptr long)
@ cdecl wined3d_device_get_raster_status(ptr long ptr)
@ cdecl wined3d_device_get_render_state(ptr long ptr)
@ cdecl wined3d_device_get_render_target(ptr long ptr)
@ cdecl wined3d_device_get_sampler_state(ptr long long ptr)
@ cdecl wined3d_device_get_scissor_rect(ptr ptr)
@ cdecl wined3d_device_get_software_vertex_processing(ptr)
@ cdecl wined3d_device_get_stream_source(ptr long ptr ptr ptr)
@ cdecl wined3d_device_get_stream_source_freq(ptr long ptr)
@ cdecl wined3d_device_get_surface_from_dc(ptr ptr ptr)
@ cdecl wined3d_device_get_swapchain(ptr long ptr)
@ cdecl wined3d_device_get_swapchain_count(ptr)
@ cdecl wined3d_device_get_texture(ptr long ptr)
@ cdecl wined3d_device_get_texture_stage_state(ptr long long ptr)
@ cdecl wined3d_device_get_transform(ptr long ptr)
@ cdecl wined3d_device_get_vertex_declaration(ptr ptr)
@ cdecl wined3d_device_get_vertex_shader(ptr)
@ cdecl wined3d_device_get_viewport(ptr ptr)
@ cdecl wined3d_device_get_vs_consts_b(ptr long ptr long)
@ cdecl wined3d_device_get_vs_consts_f(ptr long ptr long)
@ cdecl wined3d_device_get_vs_consts_i(ptr long ptr long)
@ cdecl wined3d_device_get_wined3d(ptr ptr)
@ cdecl wined3d_device_incref(ptr)
@ cdecl wined3d_device_init_3d(ptr ptr)
@ cdecl wined3d_device_init_gdi(ptr ptr)
@ cdecl wined3d_device_multiply_transform(ptr long ptr)
@ cdecl wined3d_device_present(ptr ptr ptr ptr ptr)
@ cdecl wined3d_device_process_vertices(ptr long long long ptr ptr long long)
@ cdecl wined3d_device_release_focus_window(ptr)
@ cdecl wined3d_device_reset(ptr ptr)
@ cdecl wined3d_device_restore_fullscreen_window(ptr ptr)
@ cdecl wined3d_device_set_base_vertex_index(ptr long)
@ cdecl wined3d_device_set_clip_plane(ptr long ptr)
@ cdecl wined3d_device_set_clip_status(ptr ptr)
@ cdecl wined3d_device_set_current_texture_palette(ptr long)
@ cdecl wined3d_device_set_cursor_position(ptr long long long)
@ cdecl wined3d_device_set_cursor_properties(ptr long long ptr)
@ cdecl wined3d_device_set_depth_stencil(ptr ptr)
@ cdecl wined3d_device_set_dialog_box_mode(ptr long)
@ cdecl wined3d_device_set_display_mode(ptr long ptr)
@ cdecl wined3d_device_set_gamma_ramp(ptr long long ptr)
@ cdecl wined3d_device_set_index_buffer(ptr ptr long)
@ cdecl wined3d_device_set_light(ptr long ptr)
@ cdecl wined3d_device_set_light_enable(ptr long long)
@ cdecl wined3d_device_set_material(ptr ptr)
@ cdecl wined3d_device_set_multithreaded(ptr)
@ cdecl wined3d_device_set_npatch_mode(ptr float)
@ cdecl wined3d_device_set_palette_entries(ptr long ptr)
@ cdecl wined3d_device_set_pixel_shader(ptr ptr)
@ cdecl wined3d_device_set_primitive_type(ptr long)
@ cdecl wined3d_device_set_ps_consts_b(ptr long ptr long)
@ cdecl wined3d_device_set_ps_consts_f(ptr long ptr long)
@ cdecl wined3d_device_set_ps_consts_i(ptr long ptr long)
@ cdecl wined3d_device_set_render_state(ptr long long)
@ cdecl wined3d_device_set_render_target(ptr long ptr long)
@ cdecl wined3d_device_set_sampler_state(ptr long long long)
@ cdecl wined3d_device_set_scissor_rect(ptr ptr)
@ cdecl wined3d_device_set_software_vertex_processing(ptr long)
@ cdecl wined3d_device_set_stream_source(ptr long ptr long long)
@ cdecl wined3d_device_set_stream_source_freq(ptr long long)
@ cdecl wined3d_device_set_texture(ptr long ptr)
@ cdecl wined3d_device_set_texture_stage_state(ptr long long long)
@ cdecl wined3d_device_set_transform(ptr long ptr)
@ cdecl wined3d_device_set_vertex_declaration(ptr ptr)
@ cdecl wined3d_device_set_vertex_shader(ptr ptr)
@ cdecl wined3d_device_set_viewport(ptr ptr)
@ cdecl wined3d_device_set_vs_consts_b(ptr long ptr long)
@ cdecl wined3d_device_set_vs_consts_f(ptr long ptr long)
@ cdecl wined3d_device_set_vs_consts_i(ptr long ptr long)
@ cdecl wined3d_device_setup_fullscreen_window(ptr ptr long long)
@ cdecl wined3d_device_show_cursor(ptr long)
@ cdecl wined3d_device_uninit_3d(ptr)
@ cdecl wined3d_device_uninit_gdi(ptr)
@ cdecl wined3d_device_update_surface(ptr ptr ptr ptr ptr)
@ cdecl wined3d_device_update_texture(ptr ptr ptr)
@ cdecl wined3d_device_validate_device(ptr ptr)

@ cdecl wined3d_palette_create(ptr long ptr ptr ptr)
@ cdecl wined3d_palette_decref(ptr)
@ cdecl wined3d_palette_get_entries(ptr long long long ptr)
@ cdecl wined3d_palette_get_flags(ptr)
@ cdecl wined3d_palette_get_parent(ptr)
@ cdecl wined3d_palette_incref(ptr)
@ cdecl wined3d_palette_set_entries(ptr long long long ptr)

@ cdecl wined3d_query_create(ptr long ptr)
@ cdecl wined3d_query_decref(ptr)
@ cdecl wined3d_query_get_data(ptr ptr long long)
@ cdecl wined3d_query_get_data_size(ptr)
@ cdecl wined3d_query_get_type(ptr)
@ cdecl wined3d_query_incref(ptr)
@ cdecl wined3d_query_issue(ptr long)

@ cdecl wined3d_resource_free_private_data(ptr ptr)
@ cdecl wined3d_resource_get_desc(ptr ptr)
@ cdecl wined3d_resource_get_parent(ptr)
@ cdecl wined3d_resource_get_private_data(ptr ptr ptr ptr)
@ cdecl wined3d_resource_set_private_data(ptr ptr ptr long long)

@ cdecl wined3d_rendertarget_view_create(ptr ptr ptr)
@ cdecl wined3d_rendertarget_view_decref(ptr)
@ cdecl wined3d_rendertarget_view_get_parent(ptr)
@ cdecl wined3d_rendertarget_view_get_resource(ptr)
@ cdecl wined3d_rendertarget_view_incref(ptr)

@ cdecl wined3d_shader_create_gs(ptr ptr ptr ptr ptr ptr)
@ cdecl wined3d_shader_create_ps(ptr ptr ptr ptr ptr ptr)
@ cdecl wined3d_shader_create_vs(ptr ptr ptr ptr ptr ptr)
@ cdecl wined3d_shader_decref(ptr)
@ cdecl wined3d_shader_get_byte_code(ptr ptr ptr)
@ cdecl wined3d_shader_get_parent(ptr)
@ cdecl wined3d_shader_incref(ptr)
@ cdecl wined3d_shader_set_local_constants_float(ptr long ptr long)

@ cdecl wined3d_stateblock_apply(ptr)
@ cdecl wined3d_stateblock_capture(ptr)
@ cdecl wined3d_stateblock_create(ptr long ptr)
@ cdecl wined3d_stateblock_decref(ptr)
@ cdecl wined3d_stateblock_incref(ptr)

@ cdecl wined3d_surface_blt(ptr ptr ptr ptr long ptr long)
@ cdecl wined3d_surface_bltfast(ptr long long ptr ptr long)
@ cdecl wined3d_surface_create(ptr long long long long long long long long long long long ptr ptr ptr)
@ cdecl wined3d_surface_decref(ptr)
@ cdecl wined3d_surface_flip(ptr ptr long)
@ cdecl wined3d_surface_free_private_data(ptr ptr)
@ cdecl wined3d_surface_get_blt_status(ptr long)
@ cdecl wined3d_surface_get_clipper(ptr)
@ cdecl wined3d_surface_get_flip_status(ptr long)
@ cdecl wined3d_surface_get_overlay_position(ptr ptr ptr)
@ cdecl wined3d_surface_get_palette(ptr)
@ cdecl wined3d_surface_get_parent(ptr)
@ cdecl wined3d_surface_get_pitch(ptr)
@ cdecl wined3d_surface_get_priority(ptr)
@ cdecl wined3d_surface_get_private_data(ptr ptr ptr ptr)
@ cdecl wined3d_surface_get_resource(ptr)
@ cdecl wined3d_surface_getdc(ptr ptr)
@ cdecl wined3d_surface_incref(ptr)
@ cdecl wined3d_surface_is_lost(ptr)
@ cdecl wined3d_surface_map(ptr ptr ptr long)
@ cdecl wined3d_surface_preload(ptr)
@ cdecl wined3d_surface_releasedc(ptr ptr)
@ cdecl wined3d_surface_restore(ptr)
@ cdecl wined3d_surface_set_clipper(ptr ptr)
@ cdecl wined3d_surface_set_color_key(ptr long ptr)
@ cdecl wined3d_surface_set_format(ptr long)
@ cdecl wined3d_surface_set_mem(ptr ptr)
@ cdecl wined3d_surface_set_overlay_position(ptr long long)
@ cdecl wined3d_surface_set_palette(ptr ptr)
@ cdecl wined3d_surface_set_priority(ptr long)
@ cdecl wined3d_surface_set_private_data(ptr ptr ptr long long)
@ cdecl wined3d_surface_unmap(ptr)
@ cdecl wined3d_surface_update_overlay(ptr ptr ptr ptr long ptr)
@ cdecl wined3d_surface_update_overlay_z_order(ptr long ptr)

@ cdecl wined3d_swapchain_create(ptr ptr long ptr ptr ptr)
@ cdecl wined3d_swapchain_decref(ptr)
@ cdecl wined3d_swapchain_get_back_buffer(ptr long long ptr)
@ cdecl wined3d_swapchain_get_device(ptr)
@ cdecl wined3d_swapchain_get_display_mode(ptr ptr)
@ cdecl wined3d_swapchain_get_front_buffer_data(ptr ptr)
@ cdecl wined3d_swapchain_get_gamma_ramp(ptr ptr)
@ cdecl wined3d_swapchain_get_parent(ptr)
@ cdecl wined3d_swapchain_get_present_parameters(ptr ptr)
@ cdecl wined3d_swapchain_get_raster_status(ptr ptr)
@ cdecl wined3d_swapchain_incref(ptr)
@ cdecl wined3d_swapchain_present(ptr ptr ptr ptr ptr long)
@ cdecl wined3d_swapchain_set_gamma_ramp(ptr long ptr)
@ cdecl wined3d_swapchain_set_window(ptr ptr)

@ cdecl wined3d_texture_add_dirty_region(ptr long ptr)
@ cdecl wined3d_texture_create_2d(ptr long long long long long long ptr ptr ptr)
@ cdecl wined3d_texture_create_3d(ptr long long long long long long long ptr ptr ptr)
@ cdecl wined3d_texture_create_cube(ptr long long long long long ptr ptr ptr)
@ cdecl wined3d_texture_decref(ptr)
@ cdecl wined3d_texture_free_private_data(ptr ptr)
@ cdecl wined3d_texture_generate_mipmaps(ptr)
@ cdecl wined3d_texture_get_autogen_filter_type(ptr)
@ cdecl wined3d_texture_get_level_count(ptr)
@ cdecl wined3d_texture_get_lod(ptr)
@ cdecl wined3d_texture_get_parent(ptr)
@ cdecl wined3d_texture_get_priority(ptr)
@ cdecl wined3d_texture_get_private_data(ptr ptr ptr ptr)
@ cdecl wined3d_texture_get_sub_resource(ptr long)
@ cdecl wined3d_texture_incref(ptr)
@ cdecl wined3d_texture_preload(ptr)
@ cdecl wined3d_texture_set_autogen_filter_type(ptr long)
@ cdecl wined3d_texture_set_lod(ptr long)
@ cdecl wined3d_texture_set_priority(ptr long)
@ cdecl wined3d_texture_set_private_data(ptr ptr ptr long long)

@ cdecl wined3d_vertex_declaration_create(ptr ptr long ptr ptr ptr)
@ cdecl wined3d_vertex_declaration_create_from_fvf(ptr long ptr ptr ptr)
@ cdecl wined3d_vertex_declaration_decref(ptr)
@ cdecl wined3d_vertex_declaration_get_parent(ptr)
@ cdecl wined3d_vertex_declaration_incref(ptr)

@ cdecl wined3d_volume_create(ptr long long long long long long ptr ptr ptr)
@ cdecl wined3d_volume_decref(ptr)
@ cdecl wined3d_volume_free_private_data(ptr ptr)
@ cdecl wined3d_volume_from_resource(ptr)
@ cdecl wined3d_volume_get_parent(ptr)
@ cdecl wined3d_volume_get_priority(ptr)
@ cdecl wined3d_volume_get_private_data(ptr ptr ptr ptr)
@ cdecl wined3d_volume_get_resource(ptr)
@ cdecl wined3d_volume_incref(ptr)
@ cdecl wined3d_volume_map(ptr ptr ptr long)
@ cdecl wined3d_volume_preload(ptr)
@ cdecl wined3d_volume_set_priority(ptr long)
@ cdecl wined3d_volume_set_private_data(ptr ptr ptr long long)
@ cdecl wined3d_volume_unmap(ptr)
