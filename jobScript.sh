echo "================= CMSRUN starting Step 1 ====================" >> job.log
cmsRun -j GenSimAODSim_step1.log -p PSet.py
echo "================= CMSRUN finished Step 1 ====================" >> job.log
echo "================= CMSRUN starting Step 2 ====================" >> job.log
cmsRun -e -j GenSimAODSim_step2.log miniaod_step2_cfg.py
echo "================= CMSRUN finished Step 2 ====================" >> job.log

echo "================= CMSRUN starting Step 3 ====================" >> job.log
cmsRun -e -j FrameworkJobReport.xml miniaod_step3_cfg.py
echo "================= CMSRUN finished Step 3 ====================" >> job.log

