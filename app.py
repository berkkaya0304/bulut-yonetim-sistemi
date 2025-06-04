import streamlit as st
import os
from dotenv import load_dotenv
import subprocess
import json
from datetime import datetime

# Sayfa yapılandırması
st.set_page_config(
    page_title="Huawei Cloud Yönetim Paneli",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Stilleri
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
    }
    .css-1d391kg {
        padding: 1rem;
    }
    .stSelectbox {
        padding: 0.5rem;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stTextArea>div>div>textarea {
        border-radius: 5px;
    }
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #cce5ff;
        color: #004085;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Başlık ve Üst Bilgi
st.title("☁️ Huawei Cloud Yönetim Paneli")

# Yan menü
with st.sidebar:
    # Kimlik Bilgileri Butonu
    if st.button("🔑 Kimlik Bilgilerini Yönet", use_container_width=True):
        with st.form("credentials_form"):
            st.markdown("### 🔑 Kimlik Bilgileri")
            col1, col2 = st.columns(2)
            with col1:
                access_key = st.text_input("Access Key", type="password")
                secret_key = st.text_input("Secret Key", type="password")
            with col2:
                region = st.selectbox("Bölge", ["eu-west-101", "ap-southeast-1", "na-mexico-1"])
                project_id = st.text_input("Proje ID")
            
            submitted = st.form_submit_button("Kimlik Bilgilerini Güncelle")
            if submitted:
                # Kimlik bilgilerini .env dosyasına kaydet
                with open(".env", "w") as f:
                    f.write(f"HUAWEI_ACCESS_KEY={access_key}\n")
                    f.write(f"HUAWEI_SECRET_KEY={secret_key}\n")
                    f.write(f"HUAWEI_REGION={region}\n")
                    f.write(f"HUAWEI_PROJECT_ID={project_id}\n")
                st.success("Kimlik bilgileri güncellendi!")
    
    st.markdown("---")
    
    # Ana Menü Kategorileri
    st.markdown("### 📋 Ana Menü")
    
    # Kategori seçimi
    category = st.selectbox(
        "Kategori Seçin",
        [
            "Hesaplama ve Ağ",
            "Depolama ve Veritabanı",
            "Güvenlik ve Kimlik",
            "Konteyner ve Orkestrasyon",
            "AI ve Büyük Veri",
            "Geliştirici Araçları",
            "İzleme ve Yönetim"
        ]
    )
    
    # Servis seçimi
    if category == "Hesaplama ve Ağ":
        service = st.selectbox(
            "Servis Seçin",
            [
                "ECS Yönetimi",
                "VPC Yönetimi",
                "ELB Yönetimi",
                "EIP Yönetimi",
                "NAT Gateway",
                "VPN Gateway",
                "Direct Connect",
                "Route Table"
            ]
        )
    elif category == "Depolama ve Veritabanı":
        service = st.selectbox(
            "Servis Seçin",
            [
                "OBS Yönetimi",
                "SFS Yönetimi",
                "RDS Yönetimi",
                "DCS Yönetimi",
                "DMS Yönetimi",
                "GaussDB",
                "DWS Yönetimi",
                "CSS Yönetimi"
            ]
        )
    elif category == "Güvenlik ve Kimlik":
        service = st.selectbox(
            "Servis Seçin",
            [
                "Güvenlik Grubu Yönetimi",
                "WAF Yönetimi",
                "Anti-DDoS",
                "SSL Sertifikaları",
                "IAM Yönetimi",
                "KMS Yönetimi",
                "CBR Yönetimi"
            ]
        )
    elif category == "Konteyner ve Orkestrasyon":
        service = st.selectbox(
            "Servis Seçin",
            [
                "CCE Yönetimi",
                "SWR Yönetimi",
                "ServiceStage",
                "FunctionGraph"
            ]
        )
    elif category == "AI ve Büyük Veri":
        service = st.selectbox(
            "Servis Seçin",
            [
                "ModelArts",
                "MRS Yönetimi",
                "DLS Yönetimi",
                "DGC Yönetimi",
                "CloudTable",
                "DIS Yönetimi"
            ]
        )
    elif category == "Geliştirici Araçları":
        service = st.selectbox(
            "Servis Seçin",
            [
                "DevCloud",
                "CodeArts",
                "API Gateway",
                "ServiceComb",
                "CloudIDE"
            ]
        )
    elif category == "İzleme ve Yönetim":
        service = st.selectbox(
            "Servis Seçin",
            [
                "Cloud Eye",
                "AOM Yönetimi",
                "LTS Yönetimi",
                "CES Yönetimi",
                "Terraform Durumu"
            ]
        )

    # Hızlı İşlemler
    st.markdown("### ⚡ Hızlı İşlemler")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Yenile"):
            subprocess.run(["terraform", "refresh"])
            st.success("Durum yenilendi!")
    with col2:
        if st.button("📊 Rapor"):
            try:
                from docx import Document
                from docx.shared import Inches
                import os
                from datetime import datetime
                
                # Word dosyası oluştur
                doc = Document()
                
                # Başlık
                doc.add_heading('Huawei Cloud İşlem Raporu', 0)
                doc.add_paragraph(f'Oluşturulma Tarihi: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
                
                # Terraform durumunu al
                try:
                    # Önce terraform init çalıştır
                    init_result = subprocess.run(["terraform", "init"], capture_output=True, text=True)
                    if init_result.returncode != 0:
                        doc.add_heading('Terraform Başlatma Hatası', level=2)
                        doc.add_paragraph(init_result.stderr)
                    else:
                        # Terraform durumunu al
                        state_result = subprocess.run(["terraform", "state", "list"], capture_output=True, text=True)
                        if state_result.returncode == 0:
                            doc.add_heading('Terraform Durumu', level=2)
                            doc.add_paragraph(state_result.stdout)
                        else:
                            doc.add_heading('Terraform Durumu Hatası', level=2)
                            doc.add_paragraph(state_result.stderr)
                except Exception as terraform_error:
                    doc.add_heading('Terraform Hatası', level=2)
                    doc.add_paragraph(str(terraform_error))
                
                # Son işlemler bölümü
                doc.add_heading('Son İşlemler', level=1)
                doc.add_paragraph(f'Son güncelleme: {datetime.now().strftime("%H:%M:%S")}')
                
                # Dosyayı kaydet
                report_name = f"huawei_cloud_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
                doc.save(report_name)
                
                st.success(f"Rapor oluşturuldu: {report_name}")
                
                # Dosyayı indirme linki oluştur
                with open(report_name, "rb") as file:
                    st.download_button(
                        label="📥 Raporu İndir",
                        data=file,
                        file_name=report_name,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                
            except Exception as e:
                st.error(f"Rapor oluşturulurken hata oluştu: {str(e)}")
    
    # Durum Bilgisi
    st.markdown("---")
    st.markdown("### 📊 Sistem Durumu")
    load_dotenv()
    if os.getenv("HUAWEI_ACCESS_KEY") and os.getenv("HUAWEI_SECRET_KEY"):
        st.success("✅ Kimlik bilgileri aktif")
    else:
        st.error("❌ Kimlik bilgileri eksik")
    
    # Son İşlemler
    st.markdown("### 📝 Son İşlemler")
    st.markdown(f"Son güncelleme: {datetime.now().strftime('%H:%M:%S')}")

# Hesaplama ve Ağ Kategorisi
if service == "EIP Yönetimi":
    st.header("🌐 EIP Yönetimi")
    
    eip_action = st.selectbox(
        "EIP İşlemi Seçin",
        ["EIP Oluştur", "EIP Listele", "EIP Sil", "EIP Bağla", "EIP Ayır"]
    )
    
    if eip_action == "EIP Oluştur":
        with st.form("eip_form"):
            col1, col2 = st.columns(2)
            with col1:
                eip_name = st.text_input("EIP Adı")
                bandwidth = st.number_input("Bant Genişliği (Mbps)", min_value=1, value=100)
            with col2:
                eip_type = st.selectbox("EIP Tipi", ["5_bgp", "5_sbgp"])
                charge_mode = st.selectbox("Ödeme Modu", ["traffic", "bandwidth"])
            
            submitted = st.form_submit_button("EIP Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="eip_name={eip_name}" -var="bandwidth={bandwidth}"
                -var="eip_type={eip_type}" -var="charge_mode={charge_mode}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("EIP oluşturma işlemi başlatıldı!")

elif service == "NAT Gateway":
    st.header("🌐 NAT Gateway Yönetimi")
    
    nat_action = st.selectbox(
        "NAT Gateway İşlemi Seçin",
        ["NAT Gateway Oluştur", "NAT Gateway Listele", "NAT Gateway Sil", "SNAT Kuralı Ekle", "DNAT Kuralı Ekle"]
    )
    
    if nat_action == "NAT Gateway Oluştur":
        with st.form("nat_form"):
            col1, col2 = st.columns(2)
            with col1:
                nat_name = st.text_input("NAT Gateway Adı")
                nat_type = st.selectbox("NAT Gateway Tipi", ["1", "2", "3", "4"])
            with col2:
                vpc_id = st.text_input("VPC ID")
                subnet_id = st.text_input("Subnet ID")
            
            submitted = st.form_submit_button("NAT Gateway Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="nat_name={nat_name}" -var="nat_type={nat_type}"
                -var="vpc_id={vpc_id}" -var="subnet_id={subnet_id}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("NAT Gateway oluşturma işlemi başlatıldı!")

elif service == "VPN Gateway":
    st.header("🔒 VPN Gateway Yönetimi")
    
    vpn_action = st.selectbox(
        "VPN Gateway İşlemi Seçin",
        ["VPN Gateway Oluştur", "VPN Gateway Listele", "VPN Gateway Sil", "VPN Bağlantısı Ekle"]
    )
    
    if vpn_action == "VPN Gateway Oluştur":
        with st.form("vpn_form"):
            col1, col2 = st.columns(2)
            with col1:
                vpn_name = st.text_input("VPN Gateway Adı")
                vpn_type = st.selectbox("VPN Gateway Tipi", ["Basic", "Professional"])
            with col2:
                vpc_id = st.text_input("VPC ID")
                subnet_id = st.text_input("Subnet ID")
            
            submitted = st.form_submit_button("VPN Gateway Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="vpn_name={vpn_name}" -var="vpn_type={vpn_type}"
                -var="vpc_id={vpc_id}" -var="subnet_id={subnet_id}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("VPN Gateway oluşturma işlemi başlatıldı!")

# Hesaplama ve Ağ Kategorisi - Eksik Servisler
elif service == "ECS Yönetimi":
    st.header("💻 ECS Yönetimi")
    
    ecs_action = st.selectbox(
        "ECS İşlemi Seçin",
        ["Instance Oluştur", "Instance Listele", "Instance Sil", "Instance Yeniden Başlat", "Instance Durdur"]
    )
    
    if ecs_action == "Instance Oluştur":
        with st.form("ecs_form"):
            col1, col2 = st.columns(2)
            with col1:
                instance_name = st.text_input("Instance Adı")
                image_id = st.text_input("Image ID")
                flavor = st.selectbox("Instance Tipi", ["s3.large.2", "s3.xlarge.2", "s3.2xlarge.2"])
            with col2:
                key_pair = st.text_input("SSH Key Pair")
                security_group = st.text_input("Güvenlik Grubu")
                availability_zone = st.selectbox("Bölge", ["eu-west-101a", "eu-west-101b"])
            
            submitted = st.form_submit_button("Instance Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="instance_name={instance_name}" -var="image_id={image_id}"
                -var="flavor={flavor}" -var="key_pair={key_pair}" -var="security_group={security_group}"
                -var="availability_zone={availability_zone}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("ECS instance oluşturma işlemi başlatıldı!")

elif service == "VPC Yönetimi":
    st.header("🌐 VPC Yönetimi")
    
    vpc_action = st.selectbox(
        "VPC İşlemi Seçin",
        ["VPC Oluştur", "VPC Listele", "VPC Sil", "Subnet Ekle"]
    )
    
    if vpc_action == "VPC Oluştur":
        with st.form("vpc_form"):
            col1, col2 = st.columns(2)
            with col1:
                vpc_name = st.text_input("VPC Adı")
                cidr = st.text_input("CIDR", value="192.168.0.0/16")
            with col2:
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("VPC Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="vpc_name={vpc_name}" -var="cidr={cidr}"
                -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("VPC oluşturma işlemi başlatıldı!")

elif service == "Direct Connect":
    st.header("🔌 Direct Connect Yönetimi")
    
    directconnect_action = st.selectbox(
        "Direct Connect İşlemi Seçin",
        ["Bağlantı Oluştur", "Bağlantı Listele", "Bağlantı Sil", "Virtual Interface Ekle"]
    )
    
    if directconnect_action == "Bağlantı Oluştur":
        with st.form("directconnect_form"):
            col1, col2 = st.columns(2)
            with col1:
                connection_name = st.text_input("Bağlantı Adı")
                bandwidth = st.selectbox("Bant Genişliği", ["1Gbps", "10Gbps", "40Gbps"])
            with col2:
                location = st.text_input("Lokasyon")
                provider = st.text_input("Servis Sağlayıcı")
            
            submitted = st.form_submit_button("Bağlantı Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="connection_name={connection_name}" -var="bandwidth={bandwidth}"
                -var="location={location}" -var="provider={provider}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("Direct Connect bağlantısı oluşturma işlemi başlatıldı!")

elif service == "Route Table":
    st.header("🛣️ Route Table Yönetimi")
    
    routetable_action = st.selectbox(
        "Route Table İşlemi Seçin",
        ["Route Table Oluştur", "Route Table Listele", "Route Table Sil", "Route Ekle"]
    )
    
    if routetable_action == "Route Table Oluştur":
        with st.form("routetable_form"):
            col1, col2 = st.columns(2)
            with col1:
                table_name = st.text_input("Route Table Adı")
                vpc_id = st.text_input("VPC ID")
            with col2:
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Route Table Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="table_name={table_name}" -var="vpc_id={vpc_id}"
                -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("Route Table oluşturma işlemi başlatıldı!")

# Depolama ve Veritabanı Kategorisi
elif service == "OBS Yönetimi":
    st.header("📦 Object Storage Service Yönetimi")
    
    obs_action = st.selectbox(
        "OBS İşlemi Seçin",
        ["Bucket Oluştur", "Bucket Listele", "Bucket Sil", "Object Yükle"]
    )
    
    if obs_action == "Bucket Oluştur":
        with st.form("obs_form"):
            col1, col2 = st.columns(2)
            with col1:
                bucket_name = st.text_input("Bucket Adı")
                storage_class = st.selectbox("Depolama Sınıfı", ["Standard", "Infrequent Access", "Archive"])
            with col2:
                region = st.selectbox("Bölge", ["eu-west-101", "ap-southeast-1", "na-mexico-1"])
                versioning = st.checkbox("Versiyonlama Aktif", value=False)
            
            submitted = st.form_submit_button("Bucket Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="bucket_name={bucket_name}" -var="storage_class={storage_class}"
                -var="region={region}" -var="versioning={versioning}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("OBS bucket oluşturma işlemi başlatıldı!")

elif service == "SFS Yönetimi":
    st.header("📁 Scalable File Service Yönetimi")
    
    sfs_action = st.selectbox(
        "SFS İşlemi Seçin",
        ["Dosya Sistemi Oluştur", "Dosya Sistemi Listele", "Dosya Sistemi Sil", "Erişim Kuralı Ekle"]
    )
    
    if sfs_action == "Dosya Sistemi Oluştur":
        with st.form("sfs_form"):
            col1, col2 = st.columns(2)
            with col1:
                fs_name = st.text_input("Dosya Sistemi Adı")
                size = st.number_input("Boyut (GB)", min_value=10, value=100)
            with col2:
                protocol = st.selectbox("Protokol", ["NFS", "CIFS"])
                vpc_id = st.text_input("VPC ID")
            
            submitted = st.form_submit_button("Dosya Sistemi Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="fs_name={fs_name}" -var="size={size}"
                -var="protocol={protocol}" -var="vpc_id={vpc_id}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("SFS dosya sistemi oluşturma işlemi başlatıldı!")

elif service == "RDS Yönetimi":
    st.header("🗄️ Relational Database Service Yönetimi")
    
    rds_action = st.selectbox(
        "RDS İşlemi Seçin",
        ["Instance Oluştur", "Instance Listele", "Instance Sil", "Yedekleme Oluştur"]
    )
    
    if rds_action == "Instance Oluştur":
        with st.form("rds_form"):
            col1, col2 = st.columns(2)
            with col1:
                instance_name = st.text_input("Instance Adı")
                engine = st.selectbox("Veritabanı Motoru", ["MySQL", "PostgreSQL", "SQL Server"])
            with col2:
                version = st.selectbox("Versiyon", ["5.7", "8.0", "12.0"])
                flavor = st.selectbox("Instance Tipi", ["rds.mysql.s1.large", "rds.mysql.s1.xlarge"])
            
            submitted = st.form_submit_button("Instance Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="instance_name={instance_name}" -var="engine={engine}"
                -var="version={version}" -var="flavor={flavor}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("RDS instance oluşturma işlemi başlatıldı!")

elif service == "GaussDB":
    st.header("🗄️ GaussDB Yönetimi")
    
    gauss_action = st.selectbox(
        "GaussDB İşlemi Seçin",
        ["Instance Oluştur", "Instance Listele", "Instance Sil", "Yedekleme Oluştur"]
    )
    
    if gauss_action == "Instance Oluştur":
        with st.form("gauss_form"):
            col1, col2 = st.columns(2)
            with col1:
                instance_name = st.text_input("Instance Adı")
                db_type = st.selectbox("Veritabanı Tipi", ["MySQL", "PostgreSQL"])
            with col2:
                version = st.selectbox("Versiyon", ["8.0", "9.2"])
                flavor = st.selectbox("Instance Tipi", ["gaussdb.mysql.s1.large", "gaussdb.mysql.s1.xlarge"])
            
            submitted = st.form_submit_button("Instance Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="instance_name={instance_name}" -var="db_type={db_type}"
                -var="version={version}" -var="flavor={flavor}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("GaussDB instance oluşturma işlemi başlatıldı!")

elif service == "DWS Yönetimi":
    st.header("📊 Data Warehouse Service Yönetimi")
    
    dws_action = st.selectbox(
        "DWS İşlemi Seçin",
        ["Cluster Oluştur", "Cluster Listele", "Cluster Sil", "Yedekleme Oluştur"]
    )
    
    if dws_action == "Cluster Oluştur":
        with st.form("dws_form"):
            col1, col2 = st.columns(2)
            with col1:
                cluster_name = st.text_input("Cluster Adı")
                node_type = st.selectbox("Node Tipi", ["dws.m3.xlarge", "dws.m3.2xlarge"])
            with col2:
                node_count = st.number_input("Node Sayısı", min_value=3, value=3)
                version = st.selectbox("Versiyon", ["8.1.3", "8.2.0"])
            
            submitted = st.form_submit_button("Cluster Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="cluster_name={cluster_name}" -var="node_type={node_type}"
                -var="node_count={node_count}" -var="version={version}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("DWS cluster oluşturma işlemi başlatıldı!")

elif service == "CSS Yönetimi":
    st.header("🔍 Cloud Search Service Yönetimi")
    
    css_action = st.selectbox(
        "CSS İşlemi Seçin",
        ["Cluster Oluştur", "Cluster Listele", "Cluster Sil", "Index Oluştur"]
    )
    
    if css_action == "Cluster Oluştur":
        with st.form("css_form"):
            col1, col2 = st.columns(2)
            with col1:
                cluster_name = st.text_input("Cluster Adı")
                node_type = st.selectbox("Node Tipi", ["ess.spec-2u8g", "ess.spec-4u16g"])
            with col2:
                node_count = st.number_input("Node Sayısı", min_value=1, value=3)
                version = st.selectbox("Versiyon", ["7.6.2", "7.9.3"])
            
            submitted = st.form_submit_button("Cluster Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="cluster_name={cluster_name}" -var="node_type={node_type}"
                -var="node_count={node_count}" -var="version={version}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("CSS cluster oluşturma işlemi başlatıldı!")

# Güvenlik ve Kimlik Kategorisi
elif service == "Güvenlik Grubu Yönetimi":
    st.header("🛡️ Güvenlik Grubu Yönetimi")
    
    # İşlem seçimi
    operation = st.selectbox(
        "İşlem Seçin",
        ["Güvenlik Grubu Oluştur", "Güvenlik Gruplarını Listele", "Güvenlik Grubu Sil", "Kural Ekle"]
    )
    
    if operation == "Güvenlik Grubu Oluştur":
        with st.form("security_group_create"):
            name = st.text_input("Güvenlik Grubu Adı")
            description = st.text_area("Açıklama")
            vpc_id = st.text_input("VPC ID")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="security_group_name={name}" -var="description={description}" -var="vpc_id={vpc_id}"
                """, language="bash")
                st.success("Güvenlik grubu oluşturma işlemi başlatıldı!")
                
    elif operation == "Güvenlik Gruplarını Listele":
        if st.button("Listele"):
            st.info("Terraform komutu oluşturuluyor...")
            st.code("""
terraform init
terraform state list | grep huaweicloud_networking_secgroup
            """, language="bash")
            st.success("Güvenlik grupları listeleniyor!")
            
    elif operation == "Güvenlik Grubu Sil":
        with st.form("security_group_delete"):
            group_id = st.text_input("Güvenlik Grubu ID")
            
            if st.form_submit_button("Sil"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform destroy -target=huaweicloud_networking_secgroup.{group_id}
                """, language="bash")
                st.success("Güvenlik grubu silme işlemi başlatıldı!")
                
    elif operation == "Kural Ekle":
        with st.form("security_group_rule_add"):
            group_id = st.text_input("Güvenlik Grubu ID")
            direction = st.selectbox("Yön", ["ingress", "egress"])
            protocol = st.selectbox("Protokol", ["tcp", "udp", "icmp"])
            port_range_min = st.number_input("Başlangıç Portu", min_value=1, max_value=65535)
            port_range_max = st.number_input("Bitiş Portu", min_value=1, max_value=65535)
            remote_ip_prefix = st.text_input("Uzak IP Prefix")
            
            if st.form_submit_button("Kural Ekle"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="security_group_id={group_id}" -var="direction={direction}" -var="protocol={protocol}" -var="port_range_min={port_range_min}" -var="port_range_max={port_range_max}" -var="remote_ip_prefix={remote_ip_prefix}"
                """, language="bash")
                st.success("Güvenlik grubu kuralı ekleme işlemi başlatıldı!")

elif service == "WAF Yönetimi":
    st.header("🛡️ WAF Yönetimi")
    
    # İşlem seçimi
    operation = st.selectbox(
        "İşlem Seçin",
        ["WAF Oluştur", "WAF Listele", "WAF Sil", "Kural Ekle"]
    )
    
    if operation == "WAF Oluştur":
        with st.form("waf_create"):
            name = st.text_input("WAF Adı")
            domain = st.text_input("Domain")
            server = st.text_input("Sunucu IP")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="waf_name={name}" -var="domain={domain}" -var="server={server}"
                """, language="bash")
                st.success("WAF oluşturma işlemi başlatıldı!")
                
    elif operation == "WAF Listele":
        if st.button("Listele"):
            st.info("Terraform komutu oluşturuluyor...")
            st.code("""
terraform init
terraform state list | grep huaweicloud_waf_instance
                """, language="bash")
            st.success("WAF'lar listeleniyor!")
            
    elif operation == "WAF Sil":
        with st.form("waf_delete"):
            waf_id = st.text_input("WAF ID")
            
            if st.form_submit_button("Sil"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform destroy -target=huaweicloud_waf_instance.{waf_id}
                """, language="bash")
                st.success("WAF silme işlemi başlatıldı!")
                
    elif operation == "Kural Ekle":
        with st.form("waf_rule_add"):
            waf_id = st.text_input("WAF ID")
            rule_type = st.selectbox("Kural Tipi", ["blacklist", "whitelist"])
            url = st.text_input("URL")
            action = st.selectbox("Aksiyon", ["block", "allow"])
            
            if st.form_submit_button("Kural Ekle"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="waf_id={waf_id}" -var="rule_type={rule_type}" -var="url={url}" -var="action={action}"
                """, language="bash")
                st.success("WAF kuralı ekleme işlemi başlatıldı!")

elif service == "SSL Sertifikaları":
    st.header("🔒 SSL Sertifikaları Yönetimi")
    
    # İşlem seçimi
    operation = st.selectbox(
        "İşlem Seçin",
        ["Sertifika Oluştur", "Sertifikaları Listele", "Sertifika Sil", "Sertifika Yenile"]
    )
    
    if operation == "Sertifika Oluştur":
        with st.form("ssl_create"):
            name = st.text_input("Sertifika Adı")
            domain = st.text_input("Domain")
            email = st.text_input("Email")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="ssl_name={name}" -var="domain={domain}" -var="email={email}"
                """, language="bash")
                st.success("SSL sertifikası oluşturma işlemi başlatıldı!")
                
    elif operation == "Sertifikaları Listele":
        if st.button("Listele"):
            st.info("Terraform komutu oluşturuluyor...")
            st.code("""
terraform init
terraform state list | grep huaweicloud_scm_certificate
                """, language="bash")
            st.success("SSL sertifikaları listeleniyor!")
            
    elif operation == "Sertifika Sil":
        with st.form("ssl_delete"):
            cert_id = st.text_input("Sertifika ID")
            
            if st.form_submit_button("Sil"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform destroy -target=huaweicloud_scm_certificate.{cert_id}
                """, language="bash")
                st.success("SSL sertifikası silme işlemi başlatıldı!")
                
    elif operation == "Sertifika Yenile":
        with st.form("ssl_renew"):
            cert_id = st.text_input("Sertifika ID")
            
            if st.form_submit_button("Yenile"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="cert_id={cert_id}" -var="renew=true"
                """, language="bash")
                st.success("SSL sertifikası yenileme işlemi başlatıldı!")

elif service == "IAM Yönetimi":
    st.header("👤 IAM Yönetimi")
    
    # İşlem seçimi
    operation = st.selectbox(
        "İşlem Seçin",
        ["Kullanıcı Oluştur", "Kullanıcıları Listele", "Kullanıcı Sil", "Grup Oluştur", "Rol Oluştur"]
    )
    
    if operation == "Kullanıcı Oluştur":
        with st.form("iam_user_create"):
            name = st.text_input("Kullanıcı Adı")
            email = st.text_input("Email")
            password = st.text_input("Şifre", type="password")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="user_name={name}" -var="email={email}" -var="password={password}"
                """, language="bash")
                st.success("IAM kullanıcısı oluşturma işlemi başlatıldı!")
                
    elif operation == "Kullanıcıları Listele":
        if st.button("Listele"):
            st.info("Terraform komutu oluşturuluyor...")
            st.code("""
terraform init
terraform state list | grep huaweicloud_iam_user
                """, language="bash")
            st.success("IAM kullanıcıları listeleniyor!")
            
    elif operation == "Kullanıcı Sil":
        with st.form("iam_user_delete"):
            user_id = st.text_input("Kullanıcı ID")
            
            if st.form_submit_button("Sil"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform destroy -target=huaweicloud_iam_user.{user_id}
                """, language="bash")
                st.success("IAM kullanıcısı silme işlemi başlatıldı!")
                
    elif operation == "Grup Oluştur":
        with st.form("iam_group_create"):
            name = st.text_input("Grup Adı")
            description = st.text_area("Açıklama")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="group_name={name}" -var="description={description}"
                """, language="bash")
                st.success("IAM grubu oluşturma işlemi başlatıldı!")
                
    elif operation == "Rol Oluştur":
        with st.form("iam_role_create"):
            name = st.text_input("Rol Adı")
            description = st.text_area("Açıklama")
            policy = st.text_area("Politika (JSON)")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="role_name={name}" -var="description={description}" -var="policy={policy}"
                """, language="bash")
                st.success("IAM rolü oluşturma işlemi başlatıldı!")

elif service == "Anti-DDoS":
    st.header("🛡️ Anti-DDoS Yönetimi")
    
    antiddos_action = st.selectbox(
        "Anti-DDoS İşlemi Seçin",
        ["Koruma Oluştur", "Koruma Listele", "Koruma Sil", "Kural Ekle"]
    )
    
    if antiddos_action == "Koruma Oluştur":
        with st.form("antiddos_form"):
            col1, col2 = st.columns(2)
            with col1:
                protection_name = st.text_input("Koruma Adı")
                ip_address = st.text_input("IP Adresi")
            with col2:
                protection_type = st.selectbox("Koruma Tipi", ["Basic", "Advanced", "Enterprise"])
                bandwidth = st.number_input("Bant Genişliği (Mbps)", min_value=100, value=1000)
            
            submitted = st.form_submit_button("Koruma Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="protection_name={protection_name}" -var="ip_address={ip_address}"
                -var="protection_type={protection_type}" -var="bandwidth={bandwidth}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("Anti-DDoS koruma oluşturma işlemi başlatıldı!")

# Konteyner ve Orkestrasyon Kategorisi
elif service == "ServiceStage":
    st.header("🚀 ServiceStage Yönetimi")
    
    servicestage_action = st.selectbox(
        "ServiceStage İşlemi Seçin",
        ["Uygulama Oluştur", "Uygulama Listele", "Uygulama Sil", "Dağıtım Yap"]
    )
    
    if servicestage_action == "Uygulama Oluştur":
        with st.form("servicestage_form"):
            col1, col2 = st.columns(2)
            with col1:
                app_name = st.text_input("Uygulama Adı")
                app_type = st.selectbox("Uygulama Tipi", ["Web", "Microservice", "Function"])
            with col2:
                runtime = st.selectbox("Runtime", ["Java", "Node.js", "Python", "Go"])
                framework = st.selectbox("Framework", ["Spring Boot", "Express", "Flask", "Gin"])
            
            submitted = st.form_submit_button("Uygulama Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="app_name={app_name}" -var="app_type={app_type}"
                -var="runtime={runtime}" -var="framework={framework}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("ServiceStage uygulama oluşturma işlemi başlatıldı!")

elif service == "SWR Yönetimi":
    st.header("🐳 Software Repository Yönetimi")
    
    swr_action = st.selectbox(
        "SWR İşlemi Seçin",
        ["Repository Oluştur", "Repository Listele", "Repository Sil", "Image Push"]
    )
    
    if swr_action == "Repository Oluştur":
        with st.form("swr_form"):
            col1, col2 = st.columns(2)
            with col1:
                repo_name = st.text_input("Repository Adı")
                repo_type = st.selectbox("Repository Tipi", ["Private", "Public"])
            with col2:
                description = st.text_area("Açıklama")
                category = st.selectbox("Kategori", ["Application", "Base", "Database"])
            
            submitted = st.form_submit_button("Repository Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="repo_name={repo_name}" -var="repo_type={repo_type}"
                -var="description={description}" -var="category={category}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("SWR repository oluşturma işlemi başlatıldı!")

elif service == "FunctionGraph":
    st.header("⚡ FunctionGraph Yönetimi")
    
    function_action = st.selectbox(
        "Function İşlemi Seçin",
        ["Fonksiyon Oluştur", "Fonksiyon Listele", "Fonksiyon Sil", "Trigger Ekle"]
    )
    
    if function_action == "Fonksiyon Oluştur":
        with st.form("function_form"):
            col1, col2 = st.columns(2)
            with col1:
                function_name = st.text_input("Fonksiyon Adı")
                runtime = st.selectbox("Runtime", ["Python 3.6", "Node.js 12", "Java 8"])
            with col2:
                memory = st.selectbox("Bellek (MB)", ["128", "256", "512", "1024"])
                timeout = st.number_input("Timeout (saniye)", min_value=1, value=30)
            
            submitted = st.form_submit_button("Fonksiyon Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="function_name={function_name}" -var="runtime={runtime}"
                -var="memory={memory}" -var="timeout={timeout}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("FunctionGraph fonksiyonu oluşturma işlemi başlatıldı!")

# AI ve Büyük Veri Kategorisi
elif service == "ModelArts":
    st.header("🤖 ModelArts Yönetimi")
    
    modelarts_action = st.selectbox(
        "ModelArts İşlemi Seçin",
        ["Notebook Oluştur", "Model Eğitimi Başlat", "Model Dağıtımı Yap", "Dataset Yükle"]
    )
    
    if modelarts_action == "Notebook Oluştur":
        with st.form("modelarts_form"):
            col1, col2 = st.columns(2)
            with col1:
                notebook_name = st.text_input("Notebook Adı")
                instance_type = st.selectbox("Instance Tipi", ["CPU", "GPU", "Ascend"])
            with col2:
                framework = st.selectbox("Framework", ["TensorFlow", "PyTorch", "MindSpore"])
                storage = st.number_input("Depolama (GB)", min_value=5, value=20)
            
            submitted = st.form_submit_button("Notebook Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="notebook_name={notebook_name}" -var="instance_type={instance_type}"
                -var="framework={framework}" -var="storage={storage}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("ModelArts notebook oluşturma işlemi başlatıldı!")

elif service == "DLS Yönetimi":
    st.header("📊 Data Lake Service Yönetimi")
    
    dls_action = st.selectbox(
        "DLS İşlemi Seçin",
        ["Lake Oluştur", "Lake Listele", "Lake Sil", "Dataset Ekle"]
    )
    
    if dls_action == "Lake Oluştur":
        with st.form("dls_form"):
            col1, col2 = st.columns(2)
            with col1:
                lake_name = st.text_input("Lake Adı")
                storage_type = st.selectbox("Depolama Tipi", ["Standard", "Performance"])
            with col2:
                storage_size = st.number_input("Depolama Boyutu (TB)", min_value=1, value=10)
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Lake Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="lake_name={lake_name}" -var="storage_type={storage_type}"
                -var="storage_size={storage_size}" -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("DLS lake oluşturma işlemi başlatıldı!")

# AI ve Büyük Veri Kategorisi - Eksik Servisler
elif service == "DGC Yönetimi":
    st.header("🔄 Data Governance Center Yönetimi")
    
    dgc_action = st.selectbox(
        "DGC İşlemi Seçin",
        ["Workspace Oluştur", "Workspace Listele", "Workspace Sil", "Dataset Ekle"]
    )
    
    if dgc_action == "Workspace Oluştur":
        with st.form("dgc_form"):
            col1, col2 = st.columns(2)
            with col1:
                workspace_name = st.text_input("Workspace Adı")
                workspace_type = st.selectbox("Workspace Tipi", ["Basic", "Professional"])
            with col2:
                description = st.text_area("Açıklama")
                storage_type = st.selectbox("Depolama Tipi", ["Standard", "Performance"])
            
            submitted = st.form_submit_button("Workspace Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="workspace_name={workspace_name}" -var="workspace_type={workspace_type}"
                -var="description={description}" -var="storage_type={storage_type}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("DGC workspace oluşturma işlemi başlatıldı!")

elif service == "CloudTable":
    st.header("📊 CloudTable Yönetimi")
    
    cloudtable_action = st.selectbox(
        "CloudTable İşlemi Seçin",
        ["Cluster Oluştur", "Cluster Listele", "Cluster Sil", "Table Oluştur"]
    )
    
    if cloudtable_action == "Cluster Oluştur":
        with st.form("cloudtable_form"):
            col1, col2 = st.columns(2)
            with col1:
                cluster_name = st.text_input("Cluster Adı")
                cluster_type = st.selectbox("Cluster Tipi", ["HBase", "OpenTSDB"])
            with col2:
                node_count = st.number_input("Node Sayısı", min_value=3, value=3)
                storage_type = st.selectbox("Depolama Tipi", ["SSD", "SAS"])
            
            submitted = st.form_submit_button("Cluster Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="cluster_name={cluster_name}" -var="cluster_type={cluster_type}"
                -var="node_count={node_count}" -var="storage_type={storage_type}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("CloudTable cluster oluşturma işlemi başlatıldı!")

elif service == "DIS Yönetimi":
    st.header("📥 Data Ingestion Service Yönetimi")
    
    dis_action = st.selectbox(
        "DIS İşlemi Seçin",
        ["Stream Oluştur", "Stream Listele", "Stream Sil", "Partition Ekle"]
    )
    
    if dis_action == "Stream Oluştur":
        with st.form("dis_form"):
            col1, col2 = st.columns(2)
            with col1:
                stream_name = st.text_input("Stream Adı")
                stream_type = st.selectbox("Stream Tipi", ["COMMON", "ADVANCED"])
            with col2:
                partition_count = st.number_input("Partition Sayısı", min_value=1, value=1)
                data_type = st.selectbox("Veri Tipi", ["BLOB", "JSON", "CSV"])
            
            submitted = st.form_submit_button("Stream Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="stream_name={stream_name}" -var="stream_type={stream_type}"
                -var="partition_count={partition_count}" -var="data_type={data_type}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("DIS stream oluşturma işlemi başlatıldı!")

# Geliştirici Araçları Kategorisi
elif service == "DevCloud":
    st.header("🛠️ DevCloud Yönetimi")
    
    devcloud_action = st.selectbox(
        "DevCloud İşlemi Seçin",
        ["Proje Oluştur", "Proje Listele", "Proje Sil", "Pipeline Oluştur"]
    )
    
    if devcloud_action == "Proje Oluştur":
        with st.form("devcloud_form"):
            col1, col2 = st.columns(2)
            with col1:
                project_name = st.text_input("Proje Adı")
                project_type = st.selectbox("Proje Tipi", ["Scrum", "Kanban"])
            with col2:
                visibility = st.selectbox("Görünürlük", ["Private", "Internal", "Public"])
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Proje Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="project_name={project_name}" -var="project_type={project_type}"
                -var="visibility={visibility}" -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("DevCloud proje oluşturma işlemi başlatıldı!")

elif service == "CodeArts":
    st.header("👨‍💻 CodeArts Yönetimi")
    
    codearts_action = st.selectbox(
        "CodeArts İşlemi Seçin",
        ["Proje Oluştur", "Repository Oluştur", "Pipeline Oluştur", "Build Job Oluştur"]
    )
    
    if codearts_action == "Proje Oluştur":
        with st.form("codearts_form"):
            col1, col2 = st.columns(2)
            with col1:
                project_name = st.text_input("Proje Adı")
                project_type = st.selectbox("Proje Tipi", ["Scrum", "Kanban", "Basic"])
            with col2:
                visibility = st.selectbox("Görünürlük", ["Private", "Internal", "Public"])
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Proje Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="project_name={project_name}" -var="project_type={project_type}"
                -var="visibility={visibility}" -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("CodeArts proje oluşturma işlemi başlatıldı!")

# Geliştirici Araçları Kategorisi - Eksik Servisler
elif service == "ServiceComb":
    st.header("🔄 ServiceComb Yönetimi")
    
    servicecomb_action = st.selectbox(
        "ServiceComb İşlemi Seçin",
        ["Mikroservis Oluştur", "Mikroservis Listele", "Mikroservis Sil", "API Ekle"]
    )
    
    if servicecomb_action == "Mikroservis Oluştur":
        with st.form("servicecomb_form"):
            col1, col2 = st.columns(2)
            with col1:
                service_name = st.text_input("Servis Adı")
                framework = st.selectbox("Framework", ["Spring Boot", "Go Chassis", "Java Chassis"])
            with col2:
                version = st.text_input("Versiyon", value="1.0.0")
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Mikroservis Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="service_name={service_name}" -var="framework={framework}"
                -var="version={version}" -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("ServiceComb mikroservis oluşturma işlemi başlatıldı!")

elif service == "CloudIDE":
    st.header("💻 CloudIDE Yönetimi")
    
    cloudide_action = st.selectbox(
        "CloudIDE İşlemi Seçin",
        ["Workspace Oluştur", "Workspace Listele", "Workspace Sil", "Proje Ekle"]
    )
    
    if cloudide_action == "Workspace Oluştur":
        with st.form("cloudide_form"):
            col1, col2 = st.columns(2)
            with col1:
                workspace_name = st.text_input("Workspace Adı")
                template = st.selectbox("Şablon", ["Python", "Java", "Node.js", "Go"])
            with col2:
                instance_type = st.selectbox("Instance Tipi", ["2U4G", "4U8G", "8U16G"])
                storage = st.number_input("Depolama (GB)", min_value=10, value=20)
            
            submitted = st.form_submit_button("Workspace Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="workspace_name={workspace_name}" -var="template={template}"
                -var="instance_type={instance_type}" -var="storage={storage}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("CloudIDE workspace oluşturma işlemi başlatıldı!")

# İzleme ve Yönetim Kategorisi
elif service == "Cloud Eye":
    st.header("👁️ Cloud Eye Yönetimi")
    
    cloudeye_action = st.selectbox(
        "Cloud Eye İşlemi Seçin",
        ["Alarm Kuralı Oluştur", "Dashboard Oluştur", "Metrik Görüntüle", "Rapor Oluştur"]
    )
    
    if cloudeye_action == "Alarm Kuralı Oluştur":
        with st.form("cloudeye_form"):
            col1, col2 = st.columns(2)
            with col1:
                alarm_name = st.text_input("Alarm Adı")
                metric_name = st.selectbox("Metrik", ["CPU Kullanımı", "Bellek Kullanımı", "Disk Kullanımı"])
            with col2:
                threshold = st.number_input("Eşik Değeri", min_value=0, max_value=100, value=80)
                comparison = st.selectbox("Karşılaştırma", [">", ">=", "<", "<=", "="])
            
            submitted = st.form_submit_button("Alarm Kuralı Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="alarm_name={alarm_name}" -var="metric_name={metric_name}"
                -var="threshold={threshold}" -var="comparison={comparison}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("Cloud Eye alarm kuralı oluşturma işlemi başlatıldı!")

elif service == "AOM Yönetimi":
    st.header("📈 Application Operations Management")
    
    aom_action = st.selectbox(
        "AOM İşlemi Seçin",
        ["Uygulama Ekle", "Uygulama Listele", "Uygulama Sil", "Metrik Görüntüle"]
    )
    
    if aom_action == "Uygulama Ekle":
        with st.form("aom_form"):
            col1, col2 = st.columns(2)
            with col1:
                app_name = st.text_input("Uygulama Adı")
                app_type = st.selectbox("Uygulama Tipi", ["Java", "Node.js", "Python", "Go"])
            with col2:
                environment = st.selectbox("Ortam", ["Development", "Testing", "Production"])
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Uygulama Ekle")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="app_name={app_name}" -var="app_type={app_type}"
                -var="environment={environment}" -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("AOM uygulama ekleme işlemi başlatıldı!")

elif service == "LTS Yönetimi":
    st.header("📝 Log Tank Service Yönetimi")
    
    lts_action = st.selectbox(
        "LTS İşlemi Seçin",
        ["Log Grubu Oluştur", "Log Grubu Listele", "Log Grubu Sil", "Log Stream Ekle"]
    )
    
    if lts_action == "Log Grubu Oluştur":
        with st.form("lts_form"):
            col1, col2 = st.columns(2)
            with col1:
                group_name = st.text_input("Log Grubu Adı")
                retention = st.selectbox("Saklama Süresi", ["7 gün", "30 gün", "90 gün"])
            with col2:
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Log Grubu Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="group_name={group_name}" -var="retention={retention}"
                -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("LTS log grubu oluşturma işlemi başlatıldı!")

# İzleme ve Yönetim Kategorisi - Eksik Servisler
elif service == "Terraform Durumu":
    st.header("🔄 Terraform Durumu")
    
    terraform_action = st.selectbox(
        "Terraform İşlemi Seçin",
        ["Durum Görüntüle", "Plan Oluştur", "Değişiklikleri Uygula", "Kaynakları Temizle"]
    )
    
    if terraform_action == "Durum Görüntüle":
        with st.form("terraform_form"):
            col1, col2 = st.columns(2)
            with col1:
                show_details = st.checkbox("Detayları Göster", value=True)
                output_format = st.selectbox("Çıktı Formatı", ["table", "json", "raw"])
            with col2:
                refresh = st.checkbox("Durumu Yenile", value=False)
            
            submitted = st.form_submit_button("Durum Görüntüle")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform state list
                """
                if refresh:
                    terraform_cmd += "\nterraform refresh"
                st.code(terraform_cmd, language="bash")
                st.success("Terraform durumu görüntüleme işlemi başlatıldı!")

# Güvenlik ve Kimlik Kategorisi - Eksik Servisler
elif service == "KMS Yönetimi":
    st.header("🔐 Key Management Service Yönetimi")
    
    kms_action = st.selectbox(
        "KMS İşlemi Seçin",
        ["Anahtar Oluştur", "Anahtar Listele", "Anahtar Sil", "Şifreleme/Şifre Çözme"]
    )
    
    if kms_action == "Anahtar Oluştur":
        with st.form("kms_form"):
            col1, col2 = st.columns(2)
            with col1:
                key_name = st.text_input("Anahtar Adı")
                key_type = st.selectbox("Anahtar Tipi", ["AES_256", "RSA_2048", "RSA_4096"])
            with col2:
                key_usage = st.selectbox("Kullanım Amacı", ["ENCRYPT_DECRYPT", "SIGN_VERIFY"])
                description = st.text_area("Açıklama")
            
            submitted = st.form_submit_button("Anahtar Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="key_name={key_name}" -var="key_type={key_type}"
                -var="key_usage={key_usage}" -var="description={description}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("KMS anahtarı oluşturma işlemi başlatıldı!")

elif service == "CBR Yönetimi":
    st.header("💾 Cloud Backup and Recovery Yönetimi")
    
    cbr_action = st.selectbox(
        "CBR İşlemi Seçin",
        ["Yedekleme Politikası Oluştur", "Yedekleme Listele", "Yedekleme Sil", "Geri Yükleme"]
    )
    
    if cbr_action == "Yedekleme Politikası Oluştur":
        with st.form("cbr_form"):
            col1, col2 = st.columns(2)
            with col1:
                policy_name = st.text_input("Politika Adı")
                backup_type = st.selectbox("Yedekleme Tipi", ["VM", "Disk", "SFS"])
            with col2:
                retention_days = st.number_input("Saklama Süresi (Gün)", min_value=1, value=7)
                schedule = st.selectbox("Zamanlama", ["Günlük", "Haftalık", "Aylık"])
            
            submitted = st.form_submit_button("Politika Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="policy_name={policy_name}" -var="backup_type={backup_type}"
                -var="retention_days={retention_days}" -var="schedule={schedule}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("CBR yedekleme politikası oluşturma işlemi başlatıldı!")

# Konteyner ve Orkestrasyon Kategorisi - Eksik Servisler
elif service == "CCE Yönetimi":
    st.header("🐳 Cloud Container Engine Yönetimi")
    
    cce_action = st.selectbox(
        "CCE İşlemi Seçin",
        ["Cluster Oluştur", "Cluster Listele", "Cluster Sil", "Node Pool Ekle"]
    )
    
    if cce_action == "Cluster Oluştur":
        with st.form("cce_form"):
            col1, col2 = st.columns(2)
            with col1:
                cluster_name = st.text_input("Cluster Adı")
                cluster_type = st.selectbox("Cluster Tipi", ["VirtualMachine", "BareMetal"])
            with col2:
                version = st.selectbox("Kubernetes Versiyonu", ["v1.19", "v1.21", "v1.23"])
                node_count = st.number_input("Node Sayısı", min_value=1, value=3)
            
            submitted = st.form_submit_button("Cluster Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="cluster_name={cluster_name}" -var="cluster_type={cluster_type}"
                -var="version={version}" -var="node_count={node_count}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("CCE cluster oluşturma işlemi başlatıldı!")

# Depolama ve Veritabanı Kategorisi - Eksik Servisler
elif service == "DCS Yönetimi":
    st.header("🗄️ Distributed Cache Service Yönetimi")
    
    dcs_action = st.selectbox(
        "DCS İşlemi Seçin",
        ["Instance Oluştur", "Instance Listele", "Instance Sil", "Yedekleme Oluştur"]
    )
    
    if dcs_action == "Instance Oluştur":
        with st.form("dcs_form"):
            col1, col2 = st.columns(2)
            with col1:
                instance_name = st.text_input("Instance Adı")
                engine = st.selectbox("Cache Motoru", ["Redis", "Memcached"])
            with col2:
                capacity = st.selectbox("Kapasite", ["2GB", "4GB", "8GB", "16GB"])
                flavor = st.selectbox("Instance Tipi", ["Single", "Master-Slave", "Cluster"])
            
            submitted = st.form_submit_button("Instance Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="instance_name={instance_name}" -var="engine={engine}"
                -var="capacity={capacity}" -var="flavor={flavor}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("DCS instance oluşturma işlemi başlatıldı!")

elif service == "DMS Yönetimi":
    st.header("📨 Distributed Message Service Yönetimi")
    
    dms_action = st.selectbox(
        "DMS İşlemi Seçin",
        ["Instance Oluştur", "Instance Listele", "Instance Sil", "Topic Oluştur"]
    )
    
    if dms_action == "Instance Oluştur":
        with st.form("dms_form"):
            col1, col2 = st.columns(2)
            with col1:
                instance_name = st.text_input("Instance Adı")
                engine = st.selectbox("Mesaj Motoru", ["Kafka", "RabbitMQ"])
            with col2:
                version = st.selectbox("Versiyon", ["2.3.0", "2.7.0", "3.7.0"])
                flavor = st.selectbox("Instance Tipi", ["Single", "Cluster"])
            
            submitted = st.form_submit_button("Instance Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="instance_name={instance_name}" -var="engine={engine}"
                -var="version={version}" -var="flavor={flavor}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("DMS instance oluşturma işlemi başlatıldı!")

# Hesaplama ve Ağ Kategorisi - Eksik Servisler
elif service == "ELB Yönetimi":
    st.header("⚖️ Elastic Load Balancer Yönetimi")
    
    elb_action = st.selectbox(
        "ELB İşlemi Seçin",
        ["Load Balancer Oluştur", "Load Balancer Listele", "Load Balancer Sil", "Listener Ekle"]
    )
    
    if elb_action == "Load Balancer Oluştur":
        with st.form("elb_form"):
            col1, col2 = st.columns(2)
            with col1:
                lb_name = st.text_input("Load Balancer Adı")
                lb_type = st.selectbox("Load Balancer Tipi", ["Application", "Network"])
            with col2:
                bandwidth = st.number_input("Bant Genişliği (Mbps)", min_value=1, value=100)
                flavor = st.selectbox("Instance Tipi", ["small", "medium", "large"])
            
            submitted = st.form_submit_button("Load Balancer Oluştur")
            if submitted:
                terraform_cmd = f"""
                terraform init
                terraform apply -auto-approve -var="lb_name={lb_name}" -var="lb_type={lb_type}"
                -var="bandwidth={bandwidth}" -var="flavor={flavor}"
                """
                st.code(terraform_cmd, language="bash")
                st.success("ELB load balancer oluşturma işlemi başlatıldı!")

# AI ve Büyük Veri Kategorisi - Eksik Servisler
elif service == "MRS Yönetimi":
    st.header("📊 MapReduce Service Yönetimi")
    
    # İşlem seçimi
    operation = st.selectbox(
        "İşlem Seçin",
        ["Cluster Oluştur", "Cluster Listele", "Cluster Sil", "Job Gönder"]
    )
    
    if operation == "Cluster Oluştur":
        with st.form("mrs_cluster_create"):
            name = st.text_input("Cluster Adı")
            cluster_type = st.selectbox("Cluster Tipi", ["analysis", "streaming", "hybrid"])
            node_count = st.number_input("Node Sayısı", min_value=1)
            node_flavor = st.text_input("Node Flavor")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="cluster_name={name}" -var="cluster_type={cluster_type}" -var="node_count={node_count}" -var="node_flavor={node_flavor}"
                """, language="bash")
                st.success("MRS cluster oluşturma işlemi başlatıldı!")
                
    elif operation == "Cluster Listele":
        if st.button("Listele"):
            st.info("Terraform komutu oluşturuluyor...")
            st.code("""
terraform init
terraform state list | grep huaweicloud_mrs_cluster
                """, language="bash")
            st.success("MRS cluster'ları listeleniyor!")
            
    elif operation == "Cluster Sil":
        with st.form("mrs_cluster_delete"):
            cluster_id = st.text_input("Cluster ID")
            
            if st.form_submit_button("Sil"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform destroy -target=huaweicloud_mrs_cluster.{cluster_id}
                """, language="bash")
                st.success("MRS cluster silme işlemi başlatıldı!")
                
    elif operation == "Job Gönder":
        with st.form("mrs_job_submit"):
            cluster_id = st.text_input("Cluster ID")
            job_type = st.selectbox("Job Tipi", ["MapReduce", "Spark", "Hive", "SparkScript"])
            job_name = st.text_input("Job Adı")
            jar_path = st.text_input("JAR Dosya Yolu")
            
            if st.form_submit_button("Job Gönder"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="cluster_id={cluster_id}" -var="job_type={job_type}" -var="job_name={job_name}" -var="jar_path={jar_path}"
                """, language="bash")
                st.success("MRS job gönderme işlemi başlatıldı!")

elif service == "API Gateway":
    st.header("🌐 API Gateway Yönetimi")
    
    # İşlem seçimi
    operation = st.selectbox(
        "İşlem Seçin",
        ["API Oluştur", "API Listele", "API Sil", "Environment Ekle"]
    )
    
    if operation == "API Oluştur":
        with st.form("api_create"):
            name = st.text_input("API Adı")
            group_id = st.text_input("API Group ID")
            path = st.text_input("Path")
            method = st.selectbox("Method", ["GET", "POST", "PUT", "DELETE"])
            backend_type = st.selectbox("Backend Tipi", ["HTTP", "FUNCTION"])
            backend_url = st.text_input("Backend URL")
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="api_name={name}" -var="group_id={group_id}" -var="path={path}" -var="method={method}" -var="backend_type={backend_type}" -var="backend_url={backend_url}"
                """, language="bash")
                st.success("API oluşturma işlemi başlatıldı!")
                
    elif operation == "API Listele":
        if st.button("Listele"):
            st.info("Terraform komutu oluşturuluyor...")
            st.code("""
terraform init
terraform state list | grep huaweicloud_apig_api
                """, language="bash")
            st.success("API'ler listeleniyor!")
            
    elif operation == "API Sil":
        with st.form("api_delete"):
            api_id = st.text_input("API ID")
            
            if st.form_submit_button("Sil"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform destroy -target=huaweicloud_apig_api.{api_id}
                """, language="bash")
                st.success("API silme işlemi başlatıldı!")
                
    elif operation == "Environment Ekle":
        with st.form("api_env_add"):
            group_id = st.text_input("API Group ID")
            env_name = st.text_input("Environment Adı")
            env_description = st.text_area("Environment Açıklaması")
            
            if st.form_submit_button("Environment Ekle"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="group_id={group_id}" -var="env_name={env_name}" -var="env_description={env_description}"
                """, language="bash")
                st.success("API environment ekleme işlemi başlatıldı!")

elif service == "CES Yönetimi":
    st.header("📊 Cloud Eye Service Yönetimi")
    
    # İşlem seçimi
    operation = st.selectbox(
        "İşlem Seçin",
        ["Alarm Kuralı Oluştur", "Alarm Kurallarını Listele", "Alarm Kuralı Sil", "Metrik Görüntüle"]
    )
    
    if operation == "Alarm Kuralı Oluştur":
        with st.form("ces_alarm_create"):
            name = st.text_input("Alarm Kuralı Adı")
            metric_name = st.text_input("Metrik Adı")
            threshold = st.number_input("Eşik Değeri")
            comparison_operator = st.selectbox("Karşılaştırma Operatörü", [">", "<", ">=", "<=", "="])
            period = st.number_input("Periyot (saniye)", min_value=1)
            
            if st.form_submit_button("Oluştur"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="alarm_name={name}" -var="metric_name={metric_name}" -var="threshold={threshold}" -var="comparison_operator={comparison_operator}" -var="period={period}"
                """, language="bash")
                st.success("CES alarm kuralı oluşturma işlemi başlatıldı!")
                
    elif operation == "Alarm Kurallarını Listele":
        if st.button("Listele"):
            st.info("Terraform komutu oluşturuluyor...")
            st.code("""
terraform init
terraform state list | grep huaweicloud_ces_alarmrule
                """, language="bash")
            st.success("CES alarm kuralları listeleniyor!")
            
    elif operation == "Alarm Kuralı Sil":
        with st.form("ces_alarm_delete"):
            alarm_id = st.text_input("Alarm Kuralı ID")
            
            if st.form_submit_button("Sil"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform destroy -target=huaweicloud_ces_alarmrule.{alarm_id}
                """, language="bash")
                st.success("CES alarm kuralı silme işlemi başlatıldı!")
                
    elif operation == "Metrik Görüntüle":
        with st.form("ces_metric_view"):
            metric_name = st.text_input("Metrik Adı")
            start_time = st.text_input("Başlangıç Zamanı (YYYY-MM-DD HH:MM:SS)")
            end_time = st.text_input("Bitiş Zamanı (YYYY-MM-DD HH:MM:SS)")
            
            if st.form_submit_button("Görüntüle"):
                st.info("Terraform komutu oluşturuluyor...")
                st.code(f"""
terraform init
terraform apply -var="metric_name={metric_name}" -var="start_time={start_time}" -var="end_time={end_time}"
                """, language="bash")
                st.success("CES metrik görüntüleme işlemi başlatıldı!")

# Alt bilgi
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Huawei Cloud Yönetim Paneli v2.0 | Geliştirici: Berk Kaya</p>
    <p>Son güncelleme: {}</p>
</div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True) 