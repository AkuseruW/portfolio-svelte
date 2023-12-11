import type { PageServerLoad } from './$types';
import { SERVEUR_URL } from '$env/static/private'


export const load: PageServerLoad = () => {
    const categories = async () => {
        return await fetch(`${SERVEUR_URL}/api/categories/`).then(res => res.json())
    }


    return {
        categories: categories()
    }
}