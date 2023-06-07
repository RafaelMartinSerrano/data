# Importar los módulos necesarios
from sdg.open_sdg import open_sdg_build

# Llamar a la función open_sdg_build
open_sdg_build(config='config_data.yml')

# Verificar si la clave existe en el diccionario store
if 'SDG_CUSTODIAN_AGENCIES__GLOBAL' in service.store:
    # Acceder a la clave y realizar las operaciones necesarias
    indicator_df = service.get_metadata_field_value_link(service.store['SDG_CUSTODIAN_AGENCIES__GLOBAL']['values'][service.store['SDG_CUSTODIAN_AGENCIES__GLOBAL']['indicators'][indicator]])
else:
    # Proporcionar un valor predeterminado o manejar el caso cuando la clave no se encuentra
    indicator_df = ''
