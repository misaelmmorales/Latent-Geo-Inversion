import sgems

sgems.execute('DeleteObjects SIM')
sgems.execute('DeleteObjects finished')
sgems.execute('NewCartesianGrid  SIM::128::128::16::1::1::1::0::0::0')
sgems.execute('LoadObjectFromFile filtersim_cont_channels.ti::All')
sgems.execute('DeleteObjects finished')
sgems.execute('RunGeostatAlgorithm  filtersim_cont::/GeostatParamUtils/XML::<parameters>    <algorithm name="filtersim_cont" />    <GridSelector_Sim value="SIM" />    <Property_Name_Sim value="filtersim" />    <Nb_Realizations value="20" />    <Seed value="211175" />    <PropertySelector_Training grid="TI" property="facies" />    <Scan_Template value="11 11 5" />    <Patch_Template_ADVANCED value="7 7 3" />    <Nb_Facies value="2" />    <Treat_Cate_As_Cont value="0" />    <Trans_Result value="1" />    <Hard_Data grid="" property="" />    <Use_SoftField value="0" />    <SoftData_properties count="0" value="" />    <TauModelObject value="1 1" />    <Region_Indicator_Prop value="snesim_std__real0" />    <Active_Region_Code value="" />    <Use_Previous_Simulation value="0" />    <Previous_Simulation_Prop value="snesim_std__real0" />    <Use_Region value="0" />    <Nb_Multigrids_ADVANCED value="3" />    <Debug_Level value="0" />    <Cmin_Replicates value="10 10 10" />    <Data_Weights value="0.5 0.3 0.2" />    <CrossPartition value="1" />    <KMeanPartition value="0" />    <Nb_Bins_ADVANCED value="4" />    <Nb_Bins_ADVANCED2 value="2" />    <Use_Normal_Dist value="1" />    <Use_Score_Dist value="0" />    <Filter_Default value="1" />    <Filter_User_Define value="0" />    <User_Def_Filter_File value="Data File with Filter Definition" /></parameters>')


sgems.execute('SaveGeostatGrid  SIM::filtersim.out::gslib::0::filtersim__real0::filtersim__real1::filtersim__real2::filtersim__real3::filtersim__real4::filtersim__real5::filtersim__real6::filtersim__real7::filtersim__real8::filtersim__real9::filtersim__real10::filtersim__real11::filtersim__real12::filtersim__real13::filtersim__real14::filtersim__real15::filtersim__real16::filtersim__real17::filtersim__real18::filtersim__real19')
sgems.execute('SaveGeostatGrid  SIM::filtersim.sgems::s-gems::0::filtersim__real0::filtersim__real1::filtersim__real2::filtersim__real3::filtersim__real4::filtersim__real5::filtersim__real6::filtersim__real7::filtersim__real8::filtersim__real9::filtersim__real10::filtersim__real11::filtersim__real12::filtersim__real13::filtersim__real14::filtersim__real15::filtersim__real16::filtersim__real17::filtersim__real18::filtersim__real19')


sgems.execute('NewCartesianGrid  finished::1::1::1::1.0::1.0::1.0::0::0::0')
data=[]
data.append(1)
sgems.set_property('finished','dummy',data)
sgems.execute('SaveGeostatGrid  finished::finished::gslib::0::dummy')
