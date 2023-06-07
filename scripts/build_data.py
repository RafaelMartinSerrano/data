# Importar los módulos necesarios
from sdg.open_sdg import open_sdg_build
from sdg.outputs import OutputDocumentationService

# Llamar a la función open_sdg_build
open_sdg_build(config='config_data.yml')

# Crear una instancia de OutputDocumentationService
documentation_service = OutputDocumentationService()

# Generar la documentación
documentation_service.generate_documentation()

# Obtener el MetadataReportService desde documentation_service
service = documentation_service.metadata_report_service

# Verificar si la clave existe en el diccionario store
if 'SDG_CUSTODIAN_AGENCIES__GLOBAL' in service.store:
    # Acceder a la clave y realizar las operaciones necesarias
    indicator_df = service.get_metadata_field_value_link(service.store['SDG_CUSTODIAN_AGENCIES__GLOBAL']['values'][service.store['SDG_CUSTODIAN_AGENCIES__GLOBAL']['indicators'][indicator]])
else:
    # Proporcionar un valor predeterminado o manejar el caso cuando la clave no se encuentra
    indicator_df = ''
